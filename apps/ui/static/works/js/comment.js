!function(t,e){"object"==typeof exports&&"object"==typeof module?module.exports=e():"function"==typeof define&&define.amd?define("works",[],e):"object"==typeof exports?exports.works=e():t.works=e()}(this,function(){return function(t){function e(o){if(n[o])return n[o].exports;var s=n[o]={i:o,l:!1,exports:{}};return t[o].call(s.exports,s,s.exports,e),s.l=!0,s.exports}var n={};return e.m=t,e.c=n,e.i=function(t){return t},e.d=function(t,n,o){e.o(t,n)||Object.defineProperty(t,n,{configurable:!1,enumerable:!0,get:o})},e.n=function(t){var n=t&&t.__esModule?function(){return t.default}:function(){return t};return e.d(n,"a",n),n},e.o=function(t,e){return Object.prototype.hasOwnProperty.call(t,e)},e.p="/",e(e.s=19)}({0:function(t,e){t.exports=function(t,e,n,o){var s,i=t=t||{},r=typeof t.default;"object"!==r&&"function"!==r||(s=t,i=t.default);var a="function"==typeof i?i.options:i;if(e&&(a.render=e.render,a.staticRenderFns=e.staticRenderFns),n&&(a._scopeId=n),o){var c=Object.create(a.computed||null);Object.keys(o).forEach(function(t){var e=o[t];c[t]=function(){return e}}),a.computed=c}return{esModule:s,exports:i,options:a}}},1:function(t,e,n){n(28);var o=n(0)(n(10),n(35),null,null);t.exports=o.exports},10:function(t,e,n){"use strict";Object.defineProperty(e,"__esModule",{value:!0}),e.default={name:"comment",data:function(){return{comments:[]}},computed:{count_title:function(){return this.comments.length+" 条评论"}},props:["index","notitle"],mounted:function(){var t=this;$.get("/comment?index="+this.index).success(function(e){e.success&&(t.comments=e.comments)}),load(["ui.ckeditor"],function(){CKEDITOR.config.height=100,CKEDITOR.config.extraPlugins="autogrow",CKEDITOR.config.autoGrow_minHeight=100,CKEDITOR.config.autoGrow_maxHeight=600,CKEDITOR.config.autoGrow_bottomSpace=20,CKEDITOR.config.extraPlugins="uploadimage",CKEDITOR.config.uploadUrl="/uploadfiles/upload_file?key="+t.index,CKEDITOR.config.imageUploadUrl="/uploadfiles/upload_image?key="+t.index,CKEDITOR.replace(t.$refs.content)})},methods:{save:function(){var t=this,e=CKEDITOR.instances.content.getData();if(!e)return void Alert("请输入内容");$(t.$refs.content).val(e),$.post("/comment/save?index="+t.index,$(t.$refs.form).serialize()).done(function(e){e.success&&(t.comments.push(e.data),$(t.$refs.content).val(""),CKEDITOR.instances.content.setData(""))}).fail(function(t){})}}}},19:function(t,e,n){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var o=n(1),s=n.n(o);Vue.component("Comment",s.a)},28:function(t,e){},35:function(t,e){t.exports={render:function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"box box-solid"},[t.notitle?t._e():n("div",{staticClass:"box-header with-border"},[n("h3",{staticClass:"box-title"},[t._v("评论")]),t._v(" "),n("div",{staticClass:"box-tools pull-right"},[n("span",{staticClass:"badge bg-yellow",attrs:{"data-toggle":"tooltip",title:"","data-original-title":t.count_title}},[t._v(t._s(t.count))]),t._v(" "),t._m(0)])]),t._v(" "),n("div",{staticClass:"box-body box-comments"},[t.comments.length>0?t._l(t.comments,function(e){return t.comments.length>0?n("div",{staticClass:"box-comment"},[n("img",{staticClass:"img-circle img-sm",attrs:{src:e.avator,alt:"User Image"}}),t._v(" "),n("div",{staticClass:"comment-text"},[n("span",{staticClass:"username"},[t._v("\n              "+t._s(e.author)+"\n              "),n("span",{staticClass:"text-muted pull-right"},[t._v(t._s(e.modified_time))])]),t._v(" "),n("div",{staticClass:"comment-text-content",domProps:{innerHTML:t._s(e.content)}})])]):t._e()}):[t._v("\n        暂无评论\n      ")]],2),t._v(" "),n("div",{staticClass:"box-footer"},[n("form",{ref:"form",attrs:{method:"post"}},[n("div",{staticClass:"form-group"},[n("textarea",{ref:"content",staticClass:"form-control",attrs:{name:"content",rows:"3",placeholder:"输入评论内容 ..."}})]),t._v(" "),n("div",{staticClass:"form-group"},[n("button",{staticClass:"btn btn-primary",attrs:{type:"button"},on:{click:t.save}},[t._v("保存")])])])])])},staticRenderFns:[function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("button",{staticClass:"btn btn-box-tool",attrs:{type:"button","data-widget":"collapse"}},[n("i",{staticClass:"fa fa-minus"})])}]}}})});
//# sourceMappingURL=comment.js.map