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
/******/ 	return __webpack_require__(__webpack_require__.s = 19);
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

/***/ 14:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
Object.defineProperty(__webpack_exports__, "__esModule", { value: true });


function _sort_by_modified_time(a, b) {
  return new Date(a) - new Date(b);
}
function _get_date(a) {
  var d = new Date(a);
  return d.getFullYear() + '-' + (d.getMonth() + 1) + '-' + d.getDate();
}
function _sort_by_group(tasks) {
  var groups = {},
      items;
  var last,
      item,
      i,
      _len,
      key,
      result = [];

  for (i = 0, _len = tasks.length; i < _len; i++) {
    item = tasks[i];
    key = _get_date(item['modified_time']);
    if (last === undefined || last != key) {
      items = groups[key] = [];
      last = key;
      result.push({ label: key, items: items });
    } else items = groups[key];
    items.push(item);
  }

  return result;
}

var map = {
  finish: ['fa-check bg-green', '已完成'],
  ready: ['fa-hourglass-o bg-gray', '未开始'],
  delay: ['fa-question bg-red', '延迟'],
  start: ['fa-spinner bg-blue', '进行中']
};

/* harmony default export */ __webpack_exports__["default"] = ({
  name: 'task',
  data: function data() {
    return {
      count: 0,
      origin_tasks: [],
      tasks: []
    };
  },

  computed: {
    count_title: function count_title() {
      return this.count + ' 条任务';
    },
    sorted_tasks: function sorted_tasks() {
      return _sort_by_group(this.tasks);
    }
  },
  props: ['index', 'notitle'],
  mounted: function mounted() {
    this.load();
  },

  methods: {
    load: function load() {
      var self = this;
      $.get('/task/get?index=' + this.index).success(function (r) {
        if (r.success) {
          self.tasks = r.tasks.sort(_sort_by_modified_time);
          self.count = r.tasks.length;
        }
      });
    },
    item_icon: function item_icon(item) {
      return 'fa ' + map[item.status][0];
    },
    item_title: function item_title(item) {
      return map[item.status][1];
    },
    change: function change(item, status) {
      var self = this;
      var x;
      $.post('/task/change/' + item.id, { status: status }).success(function (r) {
        if (r.success) {
          for (var i = 0, _len = self.tasks.length; i < _len; i++) {
            x = self.tasks[i];
            if (x.id == item.id) {
              self.tasks.splice(i, 1, r.data);
              self.tasks = self.tasks.sort(_sort_by_modified_time);
              return;
            }
          }
        }
      });
    }
  }
});

/***/ }),

/***/ 19:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
Object.defineProperty(__webpack_exports__, "__esModule", { value: true });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__task_Task_vue__ = __webpack_require__(7);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__task_Task_vue___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_0__task_Task_vue__);


Vue.component('Task', __WEBPACK_IMPORTED_MODULE_0__task_Task_vue___default.a);

/***/ }),

/***/ 25:
/***/ (function(module, exports) {

// removed by extract-text-webpack-plugin

/***/ }),

/***/ 30:
/***/ (function(module, exports) {

module.exports={render:function (){var _vm=this;var _h=_vm.$createElement;var _c=_vm._self._c||_h;
  return _c('div', {
    staticClass: "box box-solid"
  }, [(!_vm.notitle) ? _c('div', {
    staticClass: "box-header with-border"
  }, [_c('h3', {
    staticClass: "box-title"
  }, [_vm._v("任务")]), _vm._v(" "), _c('div', {
    staticClass: "box-tools pull-right"
  }, [_c('span', {
    staticClass: "badge bg-yellow",
    attrs: {
      "data-toggle": "tooltip",
      "title": "",
      "data-original-title": _vm.count_title
    }
  }, [_vm._v(_vm._s(_vm.count))]), _vm._v(" "), _vm._m(0)])]) : _vm._e(), _vm._v(" "), _c('div', {
    staticClass: "box-body",
    staticStyle: {
      "background-color": "#f7f7f7"
    }
  }, [_vm._l((_vm.sorted_tasks), function(task) {
    return (_vm.count > 0) ? [_c('ul', {
      staticClass: "timeline"
    }, [_c('li', {
      staticClass: "time-label"
    }, [_c('span', {
      staticClass: "bg-red"
    }, [_vm._v("\n                  " + _vm._s(task.label) + "\n                ")])]), _vm._v(" "), _vm._l((task.items), function(t) {
      return _c('li', [_c('i', {
        class: _vm.item_icon(t),
        attrs: {
          "data-original-title": _vm.item_title(t)
        }
      }), _vm._v(" "), _c('div', {
        staticClass: "timeline-item"
      }, [_c('span', {
        staticClass: "time"
      }, [_vm._v("\n                " + _vm._s(t.responsible || '未指派') + "\n                "), _c('i', {
        staticClass: "fa fa-clock-o"
      }), _vm._v(" " + _vm._s(t.modified_time) + "\n              ")]), _vm._v(" "), _c('h3', {
        staticClass: "timeline-header"
      }, [_c('a', {
        attrs: {
          "href": '/task/view/' + t.id,
          "target": "_blank"
        }
      }, [_vm._v(_vm._s(t.title))])]), _vm._v(" "), (t.content) ? _c('div', {
        staticClass: "timeline-body",
        domProps: {
          "innerHTML": _vm._s(t.content)
        }
      }) : _vm._e(), _vm._v(" "), _c('div', {
        staticClass: "timeline-footer"
      }, [(t.status == 'start') ? _c('a', {
        staticClass: "btn btn-default btn-xs",
        on: {
          "click": function($event) {
            _vm.change(t, 'finish')
          }
        }
      }, [_vm._v("完成任务")]) : _vm._e(), _vm._v(" "), (t.status == 'ready') ? _c('a', {
        staticClass: "btn btn-default btn-xs",
        on: {
          "click": function($event) {
            _vm.change(t, 'start')
          }
        }
      }, [_vm._v("开始任务")]) : _vm._e(), _vm._v(" "), (t.status == 'delay') ? _c('a', {
        staticClass: "btn btn-default btn-xs",
        on: {
          "click": function($event) {
            _vm.change(t, 'finish')
          }
        }
      }, [_vm._v("完成任务")]) : _vm._e()])])])
    })], 2)] : _vm._e()
  }), _vm._v(" "), (_vm.count == 0) ? [_vm._v("\n        暂无任务\n      ")] : _vm._e()], 2), _vm._v(" "), _c('div', {
    staticClass: "box-footer"
  }, [_c('a', {
    staticClass: "btn btn-primary",
    attrs: {
      "href": '/task/add?index=' + _vm.index,
      "target": "_blank"
    }
  }, [_vm._v("分配任务")]), _vm._v(" "), _c('button', {
    staticClass: "btn btn-info",
    on: {
      "click": _vm.load
    }
  }, [_vm._v("刷新")])])])
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

/***/ 7:
/***/ (function(module, exports, __webpack_require__) {


/* styles */
__webpack_require__(25)

var Component = __webpack_require__(0)(
  /* script */
  __webpack_require__(14),
  /* template */
  __webpack_require__(30),
  /* scopeId */
  null,
  /* cssModules */
  null
)

module.exports = Component.exports


/***/ })

/******/ });
});
//# sourceMappingURL=task.js.map