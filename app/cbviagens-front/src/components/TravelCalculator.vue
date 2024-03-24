<script setup>
import {ref} from 'vue'

const citiesModel = ref(null)
const cityNames = [
  'Google', 'Facebook', 'Twitter', 'Apple', 'Oracle'
]
const citiesOptions = ref(cityNames)

const date = ref(null)
const datePickerVisible = ref(false)
const toggleDate = () => {
  datePickerVisible.value = !datePickerVisible.value
}

const lorem = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit'
const filterFn = (val, update) => {
  if (val === '') {
    update(() => {
      citiesOptions.value = cityNames
    })
    return
  }

  update(() => {
    const needle = val.toLowerCase()
    citiesOptions.value = cityNames.filter(v => v.toLowerCase().indexOf(needle) > -1)
  })
}

const items = ref([
  {
    "id": 1,
    "name": "Expresso Oriente",
    "price_confort": "R$ 52.10",
    "price_econ": "R$ 21.50",
    "city": "São Paulo",
    "duration": "12h",
    "seat": "12C",
    "bed": "5A"
  },
  {
    "id": 2,
    "name": "Expresso Oriente",
    "price_confort": "R$ 194.20",
    "price_econ": "R$ 43.10",
    "city": "Belo Horizonte",
    "duration": "18h",
    "seat": "1A",
    "bed": "4B"
  },
])

const bestOptions = ref({
  confort: {
    "id": 1,
    "name": "Expresso Oriente",
    "price_confort": "R$ 52.10",
    "price_econ": "R$ 21.50",
    city: "São Paulo",
    duration: "12h",
    seat: "12C",
    bed: "5A"
  },
  econ: {
    id: 2,
    name: "Expresso Oriente",
    price_confort: "R$ 194.20",
    price_econ: "R$ 43.10",
    city: "Belo Horizonte",
    duration: "18h",
    seat: "1A",
    bed: "4B"
  }
})

const clear = () => {
  items.value = []
  citiesModel.value = null
  date.value = null

}


</script>

<template>

  <!--      <div class="column" style="height: 250px">-->
  <!--      <div class="col">-->
  <!--        .col-->
  <!--      </div>-->
  <!--      <div class="col-8">-->
  <!--        .col-8-->
  <!--      </div>-->
  <!--      <div class="col">-->
  <!--        .col-->
  <!--      </div>-->
  <!--    </div>-->
  <div class="row col-11 flex-center">
    <q-card row class="col-11 text-dark my-card">
      <q-card-section class="bg-primary text-brand-white row q-py-lg q-px-xl">
        <q-icon name="sym_o_local_shipping" size="2rem"></q-icon>
        <div class="text-h6 q-px-md">Calculadora de Viagens</div>

      </q-card-section>
      <q-card-section>
        <div class="column" style="height: 50vh">
          <div class="row flex flex-center col-12">
            <div class="row col-5 bg-brand-grey rounded-borders flex flex-center q-py-xl">

              <div class="row flex flex-center col-12">
                <q-icon name="fa-solid fa-hand-holding-dollar" size="1.4rem" class="q-px-md"></q-icon>
                <h6 class="text-dark">Calcule o valor da viagem</h6>
              </div>
              <q-form class="row flex flex-center col-12">
                <q-select
                  filled
                  class="row col-6 q-mb-lg"
                  v-model="citiesModel"
                  use-input
                  input-debounce="0"
                  label="Destino"
                  :options="citiesOptions"
                  @filter="filterFn"
                >
                  <template v-slot:before>
                    <q-icon name="flight_takeoff"/>
                  </template>
                  <template v-slot:no-option>
                    <q-item>
                      <q-item-section class="text-grey">
                        Nenhum destino encontrado
                      </q-item-section>
                    </q-item>
                  </template>
                </q-select>

                <div class="row col-12 flex flex-center">
                  <q-select filled v-model="date" mask="date" :rules="['date']" class="col-6" @onclick="toggleDate">
                    <q-popup-proxy class="col-12" cover transition-show="scale" transition-hide="scale">
                      <q-date v-model="date" class="col-6">
                        <div class="row items-center justify-end">
                          <q-btn v-close-popup label="Close" color="primary" flat/>
                        </div>
                      </q-date>
                    </q-popup-proxy>
                    <template v-slot:before>
                      <q-icon name="event" class="cursor-pointer">
                        <q-popup-proxy v-model="datePickerVisible" cover transition-show="scale"
                                       transition-hide="scale">
                          <!--                    <q-date v-model="date">-->
                          <!--                      <div class="row items-center justify-end">-->
                          <!--                        <q-btn v-close-popup label="Close" color="primary" flat/>-->
                          <!--                      </div>-->
                          <!--                    </q-date>-->
                        </q-popup-proxy>
                      </q-icon>
                    </template>
                  </q-select>

                </div>
              </q-form>

              <q-btn  class="q-mt-lg bg-secondary q-py-sm q-px-lg" label="Buscar" flat/>
            </div>


            <div class="row col-7 rounded-borders flex flex-center">
              <h5 v-if="!items.length" class="text-grey-7">
                Nenhum dado selecionado.
              </h5>
              <div v-else class="row col-12 flex flex-center">
                <div class="col-12 text-h6 text-center q-pa-md text-dark">Estas são as melhores alternativas de viagem
                  para
                  a data selecionada:
                </div>

                <div class="row">

                  <q-card class="row q-mx-lg q-my-lg" flat >
                    <q-card-section horizontal class="">
                      <q-card-section class="row bg-secondary text-white flex flex-center">
                        <q-icon name="fa-solid fa-hand-holding-usd col-2" size="2.1rem"></q-icon>
                      </q-card-section>
                      <q-card-section class="bg-brand-grey-darker text-center col-10">
                        <div class="text-subtitle1 text-weight-medium">
                          {{bestOptions.confort.name.toUpperCase()}}
                        </div>
                        <div class="text-body2">
                          Leito: {{bestOptions.confort.seat}} (Completo)
                        </div>
                        <div>
                          Tempo estimado: {{bestOptions.confort.duration}}
                        </div>
                      </q-card-section>

                    </q-card-section>
                  </q-card>
                  <q-card class="row q-mx-lg bg-brand-grey-darker q-my-lg flex-center" flat >
                    <q-card-section class="col-12 text-center flex flex-center q-pb-none text-weight-bold">
                      Preço:
                    </q-card-section>
                    <q-card-section class="q-pt-none">
                      {{bestOptions.confort.price_confort}}
                    </q-card-section>
                  </q-card>


                </div>

                <div class="row">

                  <q-card class="row q-mx-lg" flat bordered>
                    <q-card-section horizontal class="">
                      <q-card-section class="row bg-secondary text-white flex flex-center">
                        <q-icon name="sym_o_pace" size="2.1rem"></q-icon>
                      </q-card-section>
                      <q-card-section class="bg-brand-grey-darker text-center col-10">
                        <div class="text-subtitle1 text-weight-medium">
                          {{bestOptions.econ.name.toUpperCase()}}
                        </div>
                        <div class="text-body2">
                          Poltrona: {{bestOptions.econ.seat}}
                        </div>
                        <div>
                          Tempo estimado: {{bestOptions.econ.duration}}
                        </div>
                      </q-card-section>

                    </q-card-section>
                  </q-card>
                  <q-card class="row q-mx-lg bg-brand-grey-darker flex flex-center" flat>
                    <q-card-section class="col-12 text-center q-pb-none text-weight-bold">
                      Preço:
                    </q-card-section>
                    <q-card-section class="q-pt-none">
                      {{bestOptions.econ.price_econ}}
                    </q-card-section>
                  </q-card>
                </div>
              </div>
            </div>
          </div>
        </div>

<!--place a button here and make it go to the lower right of the card-->
        <q-card-actions align="right">
          <q-btn @click="clear" flat label="Limpar" class="bg-warning text-dark q-mt-lg q-py-sm" padding="0.5rem 1.5rem"/>
        </q-card-actions>
      </q-card-section>
    </q-card>
  </div>
</template>

<style scoped>
.rounded-borders {
  border-radius: 6px;
}

</style>
