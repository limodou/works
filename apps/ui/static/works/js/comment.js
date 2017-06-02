(function webpackUniversalModuleDefinition(root, factory) {
	if(typeof exports === 'object' && typeof module === 'object')
		module.exports = factory();
	else if(typeof define === 'function' && define.amd)
		define("works", [], factory);
	else if(typeof exports === 'object')
		exports["works"] = factory();
	else
		root["works"] = factory();
})(this, function() {
return /******/ (function(modules) { // webpackBootstrap
/******/ 	// The module cache
/******/ 	var installedModules = {};
/******/
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/
/******/ 		// Check if module is in cache
/******/ 		if(installedModules[moduleId]) {
/******/ 			return installedModules[moduleId].exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = installedModules[moduleId] = {
/******/ 			i: moduleId,
/******/ 			l: false,
/******/ 			exports: {}
/******/ 		};
/******/
/******/ 		// Execute the module function
/******/ 		modules[moduleId].call(module.exports, module, module.exports, __webpack_require__);
/******/
/******/ 		// Flag the module as loaded
/******/ 		module.l = true;
/******/
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/
/******/
/******/ 	// expose the modules object (__webpack_modules__)
/******/ 	__webpack_require__.m = modules;
/******/
/******/ 	// expose the module cache
/******/ 	__webpack_require__.c = installedModules;
/******/
/******/ 	// identity function for calling harmony imports with the correct context
/******/ 	__webpack_require__.i = function(value) { return value; };
/******/
/******/ 	// define getter function for harmony exports
/******/ 	__webpack_require__.d = function(exports, name, getter) {
/******/ 		if(!__webpack_require__.o(exports, name)) {
/******/ 			Object.defineProperty(exports, name, {
/******/ 				configurable: false,
/******/ 				enumerable: true,
/******/ 				get: getter
/******/ 			});
/******/ 		}
/******/ 	};
/******/
/******/ 	// getDefaultExport function for compatibility with non-harmony modules
/******/ 	__webpack_require__.n = function(module) {
/******/ 		var getter = module && module.__esModule ?
/******/ 			function getDefault() { return module['default']; } :
/******/ 			function getModuleExports() { return module; };
/******/ 		__webpack_require__.d(getter, 'a', getter);
/******/ 		return getter;
/******/ 	};
/******/
/******/ 	// Object.prototype.hasOwnProperty.call
/******/ 	__webpack_require__.o = function(object, property) { return Object.prototype.hasOwnProperty.call(object, property); };
/******/
/******/ 	// __webpack_public_path__
/******/ 	__webpack_require__.p = "/";
/******/
/******/ 	// Load entry module and return exports
/******/ 	return __webpack_require__(__webpack_require__.s = 15);
/******/ })
/************************************************************************/
/******/ ({

/***/ 0:
/***/ (function(module, exports) {

// this module is a runtime utility for cleaner component module output and will
// be included in the final webpack user bundle

module.exports = function normalizeComponent (
  rawScriptExports,
  compiledTemplate,
  scopeId,
  cssModules
) {
  var esModule
  var scriptExports = rawScriptExports = rawScriptExports || {}

  // ES6 modules interop
  var type = typeof rawScriptExports.default
  if (type === 'object' || type === 'function') {
    esModule = rawScriptExports
    scriptExports = rawScriptExports.default
  }

  // Vue.extend constructor export interop
  var options = typeof scriptExports === 'function'
    ? scriptExports.options
    : scriptExports

  // render functions
  if (compiledTemplate) {
    options.render = compiledTemplate.render
    options.staticRenderFns = compiledTemplate.staticRenderFns
  }

  // scopedId
  if (scopeId) {
    options._scopeId = scopeId
  }

  // inject cssModules
  if (cssModules) {
    var computed = Object.create(options.computed || null)
    Object.keys(cssModules).forEach(function (key) {
      var module = cssModules[key]
      computed[key] = function () { return module }
    })
    options.computed = computed
  }

  return {
    esModule: esModule,
    exports: scriptExports,
    options: options
  }
}


/***/ }),

/***/ 1:
/***/ (function(module, exports, __webpack_require__) {


/* styles */
__webpack_require__(23)

var Component = __webpack_require__(0)(
  /* script */
  __webpack_require__(8),
  /* template */
  __webpack_require__(28),
  /* scopeId */
  null,
  /* cssModules */
  null
)

module.exports = Component.exports


/***/ }),

/***/ 15:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
Object.defineProperty(__webpack_exports__, "__esModule", { value: true });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__comment_Comment_vue__ = __webpack_require__(1);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__comment_Comment_vue___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_0__comment_Comment_vue__);


Vue.component('Comment', __WEBPACK_IMPORTED_MODULE_0__comment_Comment_vue___default.a);

/***/ }),

/***/ 23:
/***/ (function(module, exports) {

// removed by extract-text-webpack-plugin

/***/ }),

/***/ 28:
/***/ (function(module, exports) {

module.exports={render:function (){var _vm=this;var _h=_vm.$createElement;var _c=_vm._self._c||_h;
  return _c('div', {
    staticClass: "box box-solid"
  }, [(!_vm.notitle) ? _c('div', {
    staticClass: "box-header with-border"
  }, [_c('h3', {
    staticClass: "box-title"
  }, [_vm._v("评论")]), _vm._v(" "), _c('div', {
    staticClass: "box-tools pull-right"
  }, [_c('span', {
    staticClass: "badge bg-yellow",
    attrs: {
      "data-toggle": "tooltip",
      "title": "",
      "data-original-title": _vm.count_title
    }
  }, [_vm._v(_vm._s(_vm.count))]), _vm._v(" "), _vm._m(0)])]) : _vm._e(), _vm._v(" "), _c('div', {
    staticClass: "box-body box-comments"
  }, [(_vm.comments.length > 0) ? _vm._l((_vm.comments), function(comment) {
    return (_vm.comments.length > 0) ? _c('div', {
      staticClass: "box-comment"
    }, [_c('img', {
      staticClass: "img-circle img-sm",
      attrs: {
        "src": comment.avator,
        "alt": "User Image"
      }
    }), _vm._v(" "), _c('div', {
      staticClass: "comment-text"
    }, [_c('span', {
      staticClass: "username"
    }, [_vm._v("\n              " + _vm._s(comment.author) + "\n              "), _c('span', {
      staticClass: "text-muted pull-right"
    }, [_vm._v(_vm._s(comment.modified_time))])]), _vm._v(" "), _c('div', {
      staticClass: "comment-text-content",
      domProps: {
        "innerHTML": _vm._s(comment.content)
      }
    })])]) : _vm._e()
  }) : [_vm._v("\n        暂无评论\n      ")]], 2), _vm._v(" "), _c('div', {
    staticClass: "box-footer"
  }, [_c('form', {
    ref: "form",
    attrs: {
      "method": "post"
    }
  }, [_c('div', {
    staticClass: "form-group"
  }, [_c('textarea', {
    ref: "content",
    staticClass: "form-control",
    attrs: {
      "name": "content",
      "rows": "3",
      "placeholder": "输入评论内容 ..."
    }
  })]), _vm._v(" "), _c('div', {
    staticClass: "form-group"
  }, [_c('button', {
    staticClass: "btn btn-primary",
    attrs: {
      "type": "button"
    },
    on: {
      "click": _vm.save
    }
  }, [_vm._v("保存")])])])])])
},staticRenderFns: [function (){var _vm=this;var _h=_vm.$createElement;var _c=_vm._self._c||_h;
  return _c('button', {
    staticClass: "btn btn-box-tool",
    attrs: {
      "type": "button",
      "data-widget": "collapse"
    }
  }, [_c('i', {
    staticClass: "fa fa-minus"
  })])
}]}

/***/ }),

/***/ 8:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
Object.defineProperty(__webpack_exports__, "__esModule", { value: true });


/* harmony default export */ __webpack_exports__["default"] = ({
  name: 'comment',
  data: function data() {
    return {
      comments: []
    };
  },

  computed: {
    count_title: function count_title() {
      return this.comments.length + ' 条评论';
    }
  },
  props: ['index', 'notitle'],
  mounted: function mounted() {
    var self = this;
    $.get('/comment?index=' + this.index).success(function (r) {
      if (r.success) {
        self.comments = r.comments;
      }
    });

    load(['ui.ckeditor'], function () {

      CKEDITOR.config.height = 100;

      CKEDITOR.config.extraPlugins = 'autogrow';
      CKEDITOR.config.autoGrow_minHeight = 100;
      CKEDITOR.config.autoGrow_maxHeight = 600;
      CKEDITOR.config.autoGrow_bottomSpace = 20;

      CKEDITOR.config.extraPlugins = 'uploadimage';
      CKEDITOR.config.uploadUrl = '/uploadfiles/upload_file?key=' + self.index;
      CKEDITOR.config.imageUploadUrl = '/uploadfiles/upload_image?key=' + self.index;
      CKEDITOR.replace(self.$refs.content);
    });
  },

  methods: {
    save: function save() {
      var self = this;
      var text = CKEDITOR.instances.content.getData();

      if (!text) {
        Alert('请输入内容');
        return;
      }

      $(self.$refs.content).val(text);
      $.post('/comment/save?index=' + self.index, $(self.$refs.form).serialize()).done(function (r) {
        if (r.success) {
          self.comments.push(r.data);
          $(self.$refs.content).val('');
          CKEDITOR.instances.content.setData('');
        }
      }).fail(function (r) {});
    }
  }
});

/***/ })

/******/ });
});
//# sourceMappingURL=comment.js.map