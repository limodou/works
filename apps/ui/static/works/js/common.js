!function(e,t){"object"==typeof exports&&"object"==typeof module?module.exports=t():"function"==typeof define&&define.amd?define("works",[],t):"object"==typeof exports?exports.works=t():e.works=t()}(this,function(){return function(e){function t(o){if(n[o])return n[o].exports;var s=n[o]={i:o,l:!1,exports:{}};return e[o].call(s.exports,s,s.exports,t),s.l=!0,s.exports}var n={};return t.m=e,t.c=n,t.i=function(e){return e},t.d=function(e,n,o){t.o(e,n)||Object.defineProperty(e,n,{configurable:!1,enumerable:!0,get:o})},t.n=function(e){var n=e&&e.__esModule?function(){return e.default}:function(){return e};return t.d(n,"a",n),n},t.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},t.p="/",t(t.s=20)}({0:function(e,t){e.exports=function(e,t,n,o){var s,r=e=e||{},i=typeof e.default;"object"!==i&&"function"!==i||(s=e,r=e.default);var a="function"==typeof r?r.options:r;if(t&&(a.render=t.render,a.staticRenderFns=t.staticRenderFns),n&&(a._scopeId=n),o){var l=Object.create(a.computed||null);Object.keys(o).forEach(function(e){var t=o[e];l[e]=function(){return t}}),a.computed=l}return{esModule:s,exports:r,options:a}}},11:function(e,t,n){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),t.default={name:"list-group",data:function(){return{editing:!1,selected_name:""}},props:{items:{type:Array,required:!0},selectable:{type:Boolean,default:!1},editable:{type:Boolean,default:!1},title:String},methods:{handleAdd:function(){var e={onSuccess:function(e,t){console.log("",t)}};dialog("/settings/parameter/add_category",e)},handleSelect:function(e){this.selected_name=e.name,this.$emit("selected",e.id)}}}},2:function(e,t,n){var o=n(0)(n(11),n(38),null,null);e.exports=o.exports},20:function(e,t,n){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var o=n(2),s=n.n(o);Vue.component("ListGroup",s.a)},38:function(e,t){e.exports={render:function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{staticClass:"box box-info"},[n("div",{staticClass:"box-header"},[n("h3",{staticClass:"box-title"},[e._v(e._s(e.title))]),e._v(" "),e.editable?n("div",{staticClass:"box-tools pull-right"},[n("button",{staticClass:"btn btn-box-tool",attrs:{type:"button",title:"添加"},on:{click:e.handleAdd}},[n("i",{staticClass:"fa fa-plus"})])]):e._e()]),e._v(" "),n("div",{staticClass:"box-body"},[n("ul",{staticClass:"list-group list-group-unbordered"},[0==e.items.length?n("li",{staticClass:"list-group-item text-muted"},[e._v("无内容")]):e._e(),e._v(" "),e._l(e.items,function(t){return n("a",{class:{"list-group-item":!0,active:t.name==e.selected_name},attrs:{href:"#"},on:{click:function(n){e.handleSelect(t)}}},[e._v("\n        "+e._s(t.name)+"("+e._s(t.display)+")\n        "),t.badge?n("span",{staticClass:"pull-right badge bg-blue"},[e._v(e._s(t.badge))]):e._e()])})],2)])])},staticRenderFns:[]}}})});
//# sourceMappingURL=common.js.map