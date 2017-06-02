<template>
<div class="box box-default">
    <div class="box-header with-border">
      <h3 class="box-title">信息</h3>

      <div class="box-tools pull-right">
        <button type="button" class="btn btn-box-tool" data-widget="collapse"><i class="fa fa-minus"></i>
        </button>
      </div>
    </div>
    <!-- /.box-header -->
    <div class="box-body">
      <ul class="nav nav-pills nav-stacked">
        <li>
          <a href="#">责任人
            <span class="pull-right">{{info.responsible}}</span></a>
        </li>
        <li>
          <a href="#">状态
            <span class="pull-right">{{info.status}}</span></a>
        </li>
        <li>
          <a href="#">计划时间
            <span class="pull-right">{{info.time}}</span></a>
        </li>
        <li>
          <a href="#">页面/交易数
            <span class="pull-right">{{info.page_num}} / {{info.trans_num}}</span></a>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: 'issue-info',
  data () {
    return {}
  },
  props: ['info']
}
</script>
