<template>
    <q-item clickable :to="link" active-class="text-accent">
      <q-item-section avatar>
        <q-icon :name="icon" size="1.8rem"/>
      </q-item-section>

      <q-item-section>
        <q-item-label class="text-weight-medium ">{{ title }}</q-item-label>
        <q-item-label caption>{{ caption }}</q-item-label>
      </q-item-section>

      <q-item-section side>
        <q-icon name="chevron_right" />
      </q-item-section>
    </q-item>
</template>

<script>
export default {
  name: 'EssentialLink',
  props: {
    title: {
      type: String,
      required: true
    },
    caption: {
      type: String,
      default: ''
    },
    link: {
      type: String,
      default: ''
    },
    icon: {
      type: String,
      default: ''
    }
  }
}
</script>
