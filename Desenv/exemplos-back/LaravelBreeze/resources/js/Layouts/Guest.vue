<template>
  <nav class="navbar navbar-dark bg-primary shadow-sm">
    <div class="container-fluid">
      <a class="navbar-brand m-0" href="#">
        <img
          src="/images/resultfacil3branco.png"
          alt=""
          width="80"
          class="d-inline-block align-text-top"
        />
      </a>
 
    </div>
  </nav>
  <slot />
  <nav class="navbar fixed-bottom navbar-light bg-light">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">...</a>
    </div>
  </nav>
</template>

<script>
import { Link } from "@inertiajs/inertia-vue3";

export default {
  components: {
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
