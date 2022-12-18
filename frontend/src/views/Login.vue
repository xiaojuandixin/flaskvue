<template>
  <div>
    <el-row type="flex" class="row-bg" justify="center">
      <el-col :span="8">
        <el-form ref="form" :model="form" :rules="rules" label-width="80px" class="login-form">
          <h2>私募管理人监控</h2>
          <el-form-item label="用户名" prop="username">
            <el-input v-model="form.username" autofocus></el-input>
          </el-form-item>
          <el-form-item label="密码" prop="password">
            <el-input v-model="form.password" type="password"></el-input>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="submitForm()">登录</el-button>
          </el-form-item>
        </el-form>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      form: {
        username: '',
        password: ''
      },
      rules: {
        username: [
          { required: true, message: '请输入你的用户名', trigger: 'blur' }
        ],
        password: [
          { required: true, message: '请输入你的密码', trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    submitForm() {
      axios.post('/api/login', this.form)
      .then(function (response) {
        console.log(response);
      })
      .catch(function (error) {
        console.log(error);
      });
    }
  }
}
</script>

<style>
.login-form {
  max-width: 400px;
  margin: 50px auto;
}
.login-form h2 {
  text-align: center;
  margin-bottom: 30px;
}
</style>
