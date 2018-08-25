<template>
  <v-container fluid>

    <!-- Modal -->
    <v-layout row justify-center>
      <v-dialog v-model="dialog" max-width="500px">
        <v-card>
          <v-card-title>
            <span class="headline">Cadastrar animal</span>
          </v-card-title>
          <v-card-text>
            <v-container grid-list-md>
              <v-layout wrap>
                <v-flex xs12>
                  <v-text-field label="Nome" required v-model='temp.name'></v-text-field>
                </v-flex>
                <v-flex xs12>
                  <v-text-field label="Imagem" v-model='temp.image_url' hint="http://...."></v-text-field>
                </v-flex>
              </v-layout>
            </v-container>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="blue darken-1" flat v-on:click.native="dialog = false">Fechar</v-btn>
            <v-btn color="blue darken-1" flat @click.native="addItem()">Salvar</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-layout>
    <!-- Fim do Modal -->


    <v-slide-y-transition mode="out-in">
      <v-layout row text-sm-center flex>
        
        <v-flex v-for='animal in animals' :key='animal.id' xs3 centered class="mx-4">

          <v-card>
            <v-card-media
              v-bind:src="animal.image_url"
              height="250px"
            >
            </v-card-media>

            <v-card-title primary-title>
                <div class="headline" text-sm-center>{{animal.name}}</div>
              
            </v-card-title>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn flat color="blue"  @click="removeItem(animal.id)">Delete</v-btn>
            </v-card-actions>
          </v-card>

        </v-flex>

            <v-btn
              absolute
              dark
              fab
              bottom
              right
              @click.native='dialog=true'
              color='blue'
            >
              <v-icon>add</v-icon>
            </v-btn>
      </v-layout>
    </v-slide-y-transition>
  </v-container>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  data(){
    return {
      'temp': {},
      'dialog': false,
      'animals': [
      ]
    }
  },
  methods: {
    addItem(){
      this.axios.post('http://127.0.0.1:5000/api/pet', this.temp).then((response) => {
        this.animals.push(response.data)
      })
      this.temp = {}
      this.dialog = false
    },
    removeItem(id){
      this.axios.delete('http://127.0.0.1:5000/api/pet/'+ id).then((response) => {
        this.animals.splice(id-1 ,1)
      })
      this.refreshItems()
    },
    refreshItems(){
    this.axios.get('http://127.0.0.1:5000/api/pet').then((response) => {
      this.animals = response.data.objects
    })
    },
  },
  mounted(){
    this.refreshItems()
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
