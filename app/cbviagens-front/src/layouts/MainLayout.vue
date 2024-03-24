<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated class="bg-white">
      <q-toolbar>
        <q-btn
          flat
          dense
          round
          color="primary"
          icon="menu"
          aria-label="Menu"
          @click="toggleLeftDrawer"

        />
      </q-toolbar>
    </q-header>

    <q-drawer
      v-model="leftDrawerOpen"
      show-if-above
      bordered
      class="bg-primary text-brand-white"
    >
      <q-list>
        <q-item-label header>
          <q-btn
            flat
            ripple="false"
            to="/"
            aria-label="Logo da BraSign que leva para a página principal"
          >
            <img
              width="174"
              src="~assets/logo.png"

            />
          </q-btn>
        </q-item-label>

        <EssentialLink
          v-for="link in linksList"
          :key="link.title"
          v-bind="link"
        />
      </q-list>
    </q-drawer>

    <q-page-container>
      <router-view/>
    </q-page-container>
  </q-layout>
</template>

<script setup>
import {ref} from 'vue'
import EssentialLink from 'components/EssentialLink.vue'

defineOptions({
  name: 'MainLayout'
})

const linksList = [
    {
    title: 'Página Inicial',
    icon: 'home',
    link: '/'
  },
  {
    title: 'Calculadora de Viagens',
    icon: 'sym_o_calculate',
    link: '/calc'
  },
]

const leftDrawerOpen = ref(false)

function toggleLeftDrawer() {
  leftDrawerOpen.value = !leftDrawerOpen.value
}
</script>
