<script setup>
import {ref, onMounted, onUpdated, reactive, toRefs, computed} from 'vue'
import axios from "axios";

const citiesModel = ref(null)

const date = ref(null)
const datePickerVisible = ref(false)
const toggleDate = () => {
  datePickerVisible.value = !datePickerVisible.value
}

const lorem = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit'

const filteredOptions = ref([])
const filterFn = (val, update) => {
  if (val === '') {
    update(() => {
      filteredOptions.value = []
    })
    return
  }

  update(() => {
    const needle = val.toLowerCase()
    filteredOptions.value = cityNames.value.filter(v => v.toLowerCase().indexOf(needle) > -1)
  })
}


const bestOptions = reactive({
  confort: {},
  econ: {}
})
const clear = () => {
  items.value = []
  citiesModel.value = null
  date.value = null
  bestOptions.confort = {}
  bestOptions.econ = {}


}

const state = reactive({
  items: []
})
const {items} = toRefs(state)

const fetchTransportData = async () => {
  try {
    const response = await axios.get('http://127.0.0.1:3000/api/transport/')
    return response.data
  } catch (error) {
    console.error(error)
    return null;
  }
}


const cityNames = ref([])
onMounted(async () => {
  const data = await fetchTransportData()
  if (data) {
    items.value = data
    const uniqueCityNames = new Set(data.map(item => item.city))
    cityNames.value = Array.from(uniqueCityNames)
    citiesOptions.value = cityNames.value
  }
})

const citiesOptions = computed(() => filteredOptions.value.length > 0 ? filteredOptions.value : cityNames.value)

async function onSubmit() {
  if(!citiesModel.value || !date.value) {
    dialogVisible.value = true
    return
  }
  const city = citiesModel.value
  try{
    const response = await axios.get(`http://127.0.0.1:3000/api/get_best_transport_options?city=${city}`);
    console.log(response.data)
    bestOptions.confort = response.data.confort
    bestOptions.econ = response.data.econ
  }
  catch (error) {
    console.error(error)
  }
}

const dialogVisible = ref(false)

</script>

<template>
    <q-dialog v-model="dialogVisible" backdrop-filter="brightness(60%)">
      <q-card class="q-pa-lg">

        <q-card-section class="row flex flex-center q-pa-xs">
          <q-icon name="sym_o_error" size="50px" color="accent">
          </q-icon>
        </q-card-section>
        <q-card-section class="row items-center q-pb-none text-h6 text-dark q-mb-lg">
          Insira os valores para realizar a cotação.
        </q-card-section>

        <q-card-actions align="center">
          <q-btn flat label="Fechar" class="bg-secondary" v-close-popup />
        </q-card-actions>
      </q-card>
    </q-dialog>
  <div class="row col-11 flex-center">
    <q-card row class="col-11 text-dark">
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
              <q-form class="row flex flex-center col-12" @submit="onSubmit">
                <q-select
                  filled
                  class="row col-6 q-mb-lg"
                  use-input
                  input-debounce="0"
                  v-model="citiesModel"
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
                        Nenhum dado encontrado
                      </q-item-section>
                    </q-item>
                  </template>
                </q-select>

                <div class="row col-12 flex flex-center">
                  <q-select filled v-model="date" mask="date"  class="col-6" @onclick="toggleDate">
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
                        </q-popup-proxy>
                      </q-icon>
                    </template>
                  </q-select>

                </div>
                <q-btn class="q-mt-lg bg-secondary q-py-sm q-px-lg" label="Buscar" type="submit" flat/>
              </q-form>
            </div>


            <div class="row col-7 rounded-borders flex flex-center">
              <h5 v-if="(JSON.stringify(bestOptions.confort) === '{}')" class="text-grey-7">
                Nenhum dado selecionado.
              </h5>
              <div v-else class="row col-12 flex flex-center">
                <div class="col-12 text-h6 text-center q-pa-md text-dark">Estas são as melhores alternativas de viagem
                  para
                  a data selecionada:
                </div>

                <div class="row">

                  <q-card class="row q-mx-lg q-my-lg my-card" flat>
                    <q-card-section horizontal>
                      <q-card-section class="row bg-secondary text-white flex flex-center">
                        <q-icon name="fa-solid fa-hand-holding-usd col-2" size="2.1rem"></q-icon>
                      </q-card-section>
                      <q-card-section class="bg-brand-grey-darker text-center col-10">
                        <div class="text-subtitle1 text-weight-medium">
                          {{ bestOptions.confort.name.toUpperCase() }}
                        </div>
                        <div class="text-body2">
                          Leito: {{ bestOptions.confort.bed }} (Completo)
                        </div>
                        <div>
                          Tempo estimado: {{ bestOptions.confort.duration }}
                        </div>
                      </q-card-section>

                    </q-card-section>
                  </q-card>
                  <q-card class="row q-mx-lg bg-brand-grey-darker q-my-lg flex-center my-card" flat>
                    <q-card-section class="col-12 text-center flex flex-center q-pb-none text-weight-bold">
                      Preço:
                    </q-card-section>
                    <q-card-section class="q-pt-none">
                      R$ {{ bestOptions.confort.price_confort }}
                    </q-card-section>
                  </q-card>


                </div>

                <div class="row">

                  <q-card class="row q-mx-lg my-card" flat bordered>
                    <q-card-section horizontal>
                      <q-card-section class="row bg-secondary text-white flex flex-center">
                        <q-icon name="sym_o_pace" size="2.1rem"></q-icon>
                      </q-card-section>
                      <q-card-section class="bg-brand-grey-darker text-center col-10">
                        <div class="text-subtitle1 text-weight-medium">
                          {{ bestOptions.econ.name.toUpperCase() }}
                        </div>
                        <div class="text-body2">
                          Poltrona: {{ bestOptions.econ.seat }}
                        </div>
                        <div>
                          Tempo estimado: {{ bestOptions.econ.duration }}
                        </div>
                      </q-card-section>

                    </q-card-section>
                  </q-card>
                  <q-card class="row q-mx-lg bg-brand-grey-darker flex flex-center" flat>
                    <q-card-section class="col-12 text-center q-pb-none text-weight-bold">
                      Preço:
                    </q-card-section>
                    <q-card-section class="q-pt-none">
                      R$ {{ bestOptions.econ.price_econ }}
                    </q-card-section>
                  </q-card>
                </div>
              </div>
            </div>
          </div>
        </div>

        <q-card-actions align="right">
          <q-btn @click="clear" flat label="Limpar" class="bg-warning text-dark q-mt-lg q-py-sm"
                 padding="0.5rem 1.5rem"/>
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
