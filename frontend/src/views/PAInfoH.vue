<template>
<div>
    <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect">
    <el-menu-item index="1">用户管理</el-menu-item>
    <el-menu-item index="2">注销产品户信息查询</el-menu-item>
    <el-menu-item index="3">日志查询</el-menu-item>
    </el-menu>
</div>
</template>
      
<script>
import axios from 'axios'
import Cookies from 'js-cookie'
  
export default {
    data() {
        return {
            activeIndex: '2'
        }
    },
    methods: {
        handleSelect(index) {
            let self = this
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
                if (index === '1') {
                    self.$router.push('/home');
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
        console.log("hello")
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