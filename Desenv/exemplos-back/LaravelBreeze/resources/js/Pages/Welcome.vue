<template>
  <Head title="Welcome" />
 <h1>WELCOME</h1>
  
<div>
          <div v-if="$page.props.auth.user">
            <Link href="/dashboard">
              <i class="fas fa-home" /><span>DASHBOARD</span>
            </Link>
          </div>

          <div v-if="canLogin">
            <Link :href="route('login')">
              <i class="fas fa-sign-in-alt" /><span>LOGIN</span>
            </Link>
          </div>

          <div v-if="canRegister">
            <Link :href="route('register')">
              <i class="fas fa-user" /><span>REGISTER</span>
            </Link>
          </div>
        </div>

</template>

<script>
import { Head, Link } from "@inertiajs/inertia-vue3";
import AppGuestLayout from '@/Layouts/Guest.vue'
import AppLogoFull from "@/Components/LogoFull.vue";
export default {
  layout: AppGuestLayout,  
  components: {
    AppLogoFull,
    Head,
    Link,
  },
  props: {
    canLogin: Boolean,
    canRegister: Boolean,
    laravelVersion: String,
    phpVersion: String,
  },
};
</script>
