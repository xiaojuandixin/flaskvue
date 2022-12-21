<template>
  <div>
    <el-menu default-active="1" class="el-menu-demo" mode="horizontal">
      <el-menu-item index="1">用户管理</el-menu-item>
      <el-menu-item index="2">注销产品户信息查询</el-menu-item>
      <el-menu-item index="3">日志查询</el-menu-item>
    </el-menu>

    <el-form class="form-demo" ref="form" :model="form" label-width="80px">
      <div class="row"><div class="col">&nbsp;</div></div>
      <div class="row"><div class="col">&nbsp;</div></div>
      <div class="row"><div class="col">&nbsp;</div></div>
      <div class="row"><div class="col">&nbsp;</div></div>

      <el-form-item label="用户名: "> 
        <el-input v-model="form.name" placeholder="" style="width: 250px" readonly="true"></el-input>
      </el-form-item>
      <el-form-item label="用户角色: "> 
        <el-input v-model="form.role" placeholder="" style="width: 250px" readonly="true"></el-input>
      </el-form-item>
      <el-form-item label="邮箱：">
        <el-input v-model="form.email" placeholder="请输入邮箱" style="width: 250px; background-color: red;" ></el-input>
      </el-form-item>
      <el-form-item label="密码：">
        <el-input v-model="form.pwd" placeholder="请输入密码 (默认不变)" style="width: 250px; background-color: red;" type=password></el-input>
      </el-form-item>

      <div class="row"><div class="col">&nbsp;</div></div>

      <el-form-item>
        <el-button type="primary" @click="onSubmit">保存</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>
    
<script>
// import axios from 'axios'
import Cookies from 'js-cookie'

  export default {
    data() {
      return {
        form: {
          name: 'dixin.fan',
          role: 'sales',
          email: 'dishan@mail.ustc.edu.cn',
          pwd: ''
        },
      }
    },
    methods: {
      onSubmit() {
        alert('helo')
      },
    },
    mounted() {
      if (Cookies.get('info') !== undefined) {
        const info = JSON.parse(Cookies.get('info'));
        alert(info['uid'])
      } else {
        alert('用户未登录,请返回登陆')
        this.$router.push('/');
      }
    }
  }
</script>


<style>
.el-menu-demo {
  display: flex;
  justify-content: center;
}
.form-demo {
  margin-left: 450px;
}
</style>