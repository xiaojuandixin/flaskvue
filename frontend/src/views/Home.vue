<template>
  <div>
    <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect">
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
        <el-input :placeholder="form.name" style="width: 250px" readonly="true"></el-input>
      </el-form-item>
      <el-form-item label="用户角色: "> 
        <el-input :placeholder="form.role" style="width: 250px" readonly="true"></el-input>
      </el-form-item>
      <el-form-item label="邮箱：">
        <el-input v-model="form.email" placeholder="请输入邮箱" style="width: 250px; "></el-input>
      </el-form-item>
      <el-form-item label="新密码：">
        <el-input v-model="form.pwd" placeholder="" style="width: 250px; " type=password></el-input>
      </el-form-item>

      <div class="row"><div class="col">&nbsp;</div></div>

      <el-form-item>
        <el-button type="primary" @click="onSubmit">修改</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>
    
<script>
import axios from 'axios'
import Cookies from 'js-cookie'

  export default {
    data() {
      return {
        form: {
          uid: '',
          name: '',
          role: '',
          email: '',
          pwd: '',
          origin_email: ''
        },
        activeIndex: '1'
      }
    },
    methods: {
      onSubmit() {
        let self = this
        if (!this.isEmail(this.form.email)) {
          alert("邮箱格式不符合规范")
          return
        } 
        if ((this.form.email !== this.form.origin_email) || (this.form.pwd.length !== 0)) {
          var r = confirm("确认对信息进行修改?");
          if (r == true) {
              const old_token = Cookies.get('token')
              axios.post('/api/editInfo', {
                new_email: this.form.email,
                new_pwd: this.form.pwd,
                token: old_token
              })
              .then(function (response) {
                const code = response.data['code']
                const msg = response.data['msg']
                if (code === 200) {
                  const new_token = response.data['new_token']
                  Cookies.set('token', new_token, { expires: 7 });

                  const new_email = response.data['new_email']
                  const info = JSON.parse(Cookies.get('info'));
                  info['email'] = new_email
                  const jsonData = JSON.stringify(info)
                  Cookies.set('info', jsonData, { expires: 7 });
                  alert(msg)
                }else {
                  alert(msg+",请返回登陆")
                  self.$router.push('/');
                }
              })
              .catch(function (error) {
                console.log(error);
              });
          } else {
              return
          }
        } else {
          alert("未修改任何信息")
          return
        }
      },
      isEmail(str) {
        // 定义邮箱地址的正则表达式
        const emailRegex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$/;
        // 使用 test 方法测试字符串是否匹配邮箱地址的正则表达式
        return emailRegex.test(str);
      },
      handleSelect(index) {
        let self = this
        // alert(this.form.role)
        // console.log(index)
        const old_token = Cookies.get('token')
        axios.post('/api/refreshToken', {
          token: old_token
        })
        .then(function (response) {
          const code = response.data['code']
          const msg = response.data['msg']
          if (code === 200) {
            const new_token = response.data['new_token']
            Cookies.set('token', new_token, { expires: 7 });
            // alert('hello')
            // alert(index)
            if (index === '2') {
              if (self.form.role === 'head') {
                self.$router.push('/painfoh');
              } else if (self.form.role === 'sale') {
                self.$router.push('/painfos');
              }
            }
          }else {
            alert(msg+",请返回登陆")
            self.$router.push('/');
          }
        })
        .catch(function (error) {
          console.log(error);
        });
      }
    },
    mounted() {
      if (Cookies.get('info') !== undefined) {
        const info = JSON.parse(Cookies.get('info'));
        this.form.uid = info['uid']
        this.form.name = info['name']
        this.form.role = info['role']
        this.form.email = info['email']
        this.form.origin_email = info['email']
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