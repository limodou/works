!function(t,e){"object"==typeof exports&&"object"==typeof module?module.exports=e():"function"==typeof define&&define.amd?define("works",[],e):"object"==typeof exports?exports.works=e():t.works=e()}(this,function(){return function(t){function e(n){if(s[n])return s[n].exports;var i=s[n]={i:n,l:!1,exports:{}};return t[n].call(i.exports,i,i.exports,e),i.l=!0,i.exports}var s={};return e.m=t,e.c=s,e.i=function(t){return t},e.d=function(t,s,n){e.o(t,s)||Object.defineProperty(t,s,{configurable:!1,enumerable:!0,get:n})},e.n=function(t){var s=t&&t.__esModule?function(){return t.default}:function(){return t};return e.d(s,"a",s),s},e.o=function(t,e){return Object.prototype.hasOwnProperty.call(t,e)},e.p="/",e(e.s=24)}({0:function(t,e){t.exports=function(t,e,s,n){var i,a=t=t||{},o=typeof t.default;"object"!==o&&"function"!==o||(i=t,a=t.default);var r="function"==typeof a?a.options:a;if(e&&(r.render=e.render,r.staticRenderFns=e.staticRenderFns),s&&(r._scopeId=s),n){var c=Object.create(r.computed||null);Object.keys(n).forEach(function(t){var e=n[t];c[t]=function(){return e}}),r.computed=c}return{esModule:i,exports:a,options:r}}},18:function(t,e,s){"use strict";function n(t,e){return new Date(t.modified_time.substr(0,10))-new Date(e.modified_time.substr(0,10))}function i(t){var e=new Date(t.substr(0,10));return e.getFullYear()+"-"+(e.getMonth()+1)+"-"+e.getDate()}function a(t){var e,s,n,a,o,r,c={},u=[];for(a=0,o=t.length;a<o;a++)n=t[a],r=i(n.modified_time),void 0===s||s!=r?(e=c[r]=[],s=r,u.push({label:r,items:e})):e=c[r],e.push(n);return u}Object.defineProperty(e,"__esModule",{value:!0});var o={finish:["fa-check bg-green","已完成"],ready:["fa-hourglass-o bg-gray","未开始"],delay:["fa-question bg-red","延迟"],start:["fa-spinner bg-blue","进行中"]};e.default={name:"task",data:function(){return{count:0,origin_tasks:[],tasks:[]}},computed:{count_title:function(){return this.count+" 条任务"},sorted_tasks:function(){return a(this.tasks)}},props:["index","notitle"],mounted:function(){this.load()},methods:{load:function(){var t=this;$.get("/task/get?index="+this.index).success(function(e){e.success&&(t.tasks=e.tasks.sort(n),t.count=e.tasks.length)})},item_icon:function(t){return"fa "+o[t.status][0]},item_title:function(t){return o[t.status][1]},change:function(t,e){var s,i=this;$.post("/task/change/"+t.id,{status:e}).success(function(e){if(e.success)for(var a=0,o=i.tasks.length;a<o;a++)if(s=i.tasks[a],s.id==t.id)return i.tasks.splice(a,1,e.data),void(i.tasks=i.tasks.sort(n))})}}}},24:function(t,e,s){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var n=s(9),i=s.n(n);Vue.component("Task",i.a)},30:function(t,e){},37:function(t,e){t.exports={render:function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",{staticClass:"box box-solid"},[t.notitle?t._e():s("div",{staticClass:"box-header with-border"},[s("h3",{staticClass:"box-title"},[t._v("任务")]),t._v(" "),s("div",{staticClass:"box-tools pull-right"},[s("span",{staticClass:"badge bg-yellow",attrs:{"data-toggle":"tooltip",title:"","data-original-title":t.count_title}},[t._v(t._s(t.count))]),t._v(" "),t._m(0)])]),t._v(" "),s("div",{staticClass:"box-body",staticStyle:{"background-color":"#f7f7f7"}},[t._l(t.sorted_tasks,function(e){return t.count>0?[s("ul",{staticClass:"timeline"},[s("li",{staticClass:"time-label"},[s("span",{staticClass:"bg-red"},[t._v("\n                  "+t._s(e.label)+"\n                ")])]),t._v(" "),t._l(e.items,function(e){return s("li",[s("i",{class:t.item_icon(e),attrs:{"data-original-title":t.item_title(e)}}),t._v(" "),s("div",{staticClass:"timeline-item"},[s("span",{staticClass:"time"},[t._v("\n                "+t._s(e.responsible||"未指派")+"\n                "),s("i",{staticClass:"fa fa-clock-o"}),t._v(" "+t._s(e.modified_time)+"\n              ")]),t._v(" "),s("h3",{staticClass:"timeline-header"},[s("a",{attrs:{href:"/task/view/"+e.id,target:"_blank"}},[t._v(t._s(e.title))])]),t._v(" "),e.content?s("div",{staticClass:"timeline-body",domProps:{innerHTML:t._s(e.content)}}):t._e(),t._v(" "),s("div",{staticClass:"timeline-footer"},["start"==e.status?s("a",{staticClass:"btn btn-default btn-xs",on:{click:function(s){t.change(e,"finish")}}},[t._v("完成任务")]):t._e(),t._v(" "),"ready"==e.status?s("a",{staticClass:"btn btn-default btn-xs",on:{click:function(s){t.change(e,"start")}}},[t._v("开始任务")]):t._e(),t._v(" "),"delay"==e.status?s("a",{staticClass:"btn btn-default btn-xs",on:{click:function(s){t.change(e,"finish")}}},[t._v("完成任务")]):t._e()])])])})],2)]:t._e()}),t._v(" "),0==t.count?[t._v("\n        暂无任务\n      ")]:t._e()],2),t._v(" "),s("div",{staticClass:"box-footer"},[s("a",{staticClass:"btn btn-primary",attrs:{href:"/task/add?index="+t.index,target:"_blank"}},[t._v("分配任务")]),t._v(" "),s("button",{staticClass:"btn btn-info",on:{click:t.load}},[t._v("刷新")])])])},staticRenderFns:[function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("button",{staticClass:"btn btn-box-tool",attrs:{type:"button","data-widget":"collapse"}},[s("i",{staticClass:"fa fa-minus"})])}]}},9:function(t,e,s){s(30);var n=s(0)(s(18),s(37),null,null);t.exports=n.exports}})});
//# sourceMappingURL=task.js.map