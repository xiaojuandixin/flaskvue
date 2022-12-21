<template>
  <div>
    <el-menu class="el-menu-demo" mode="horizontal">
      <el-menu-item index="1">用户管理</el-menu-item>
      <el-menu-item index="2">注销产品户信息查询</el-menu-item>
      <el-menu-item index="3">日志查询</el-menu-item>
    </el-menu>

    <el-form class="form-demo" ref="form" :model="form" label-width="80px">
      <el-form-item label="用户名">
        <el-input v-model="form.name" placeholder="请输入用户名"></el-input>
      </el-form-item>
      <el-form-item label="邮箱">
        <el-input v-model="form.email" placeholder="请输入邮箱"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onSubmit">保存</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>
    
<script>
  export default {
    data() {
      return {
        form: {
          name: '',
          email: '',
        },
      }
    },
    methods: {
      onSubmit() {
        // 在此处执行保存用户信息的逻辑
      },
    },
  }
</script>


<style>
.el-menu-demo {
  display: flex;
  justify-content: center;
}
.form-demo {
  display: flex;
  justify-content: center;
}
</style>
    