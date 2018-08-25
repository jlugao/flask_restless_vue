<template>
  <v-app app>

    <!-- Toolbar -->
    <v-toolbar >
      <v-spacer></v-spacer>
      <v-toolbar-title >Pet Shop</v-toolbar-title>
      <v-spacer></v-spacer>
    </v-toolbar>
    <!-- Fim do toolbar -->

    <v-content>
      <HelloWorld/>
    </v-content>


  </v-app>
</template>

<script>
import HelloWorld from './components/HelloWorld'

export default {
  name: 'App',
  components: {
    HelloWorld
  },
  data () {
    return {

    }
  }
}
</script>
