<!--<template>-->
<!--  <q-page class="row flex-center">-->


<!--  </q-page>-->
<!--</template>-->

<!--<script setup>-->
<!--import TravelCalculator from 'components/TravelCalculator.vue';-->
<!--defineOptions({-->
<!--  name: 'IndexPage'-->
<!--});-->
<!--</script>-->

<template>
  <div class="index-page text-dark">
    <!-- Hero section -->
    <div class="hero-section">
      <div class="hero-content">
        <h1>Bem vindo ao CBViagens</h1>
        <p>Embarque em uma experiência de viagem revolucionária.</p>
        <q-btn to="/calc" color="secondary" class="q-mr-md">Experimente</q-btn>
        <q-btn color="primary" label="Aprenda mais" @click="scrollToSection('features')" />
      </div>
      <div class="hero-image">
        <q-img src="hero_img.jpg" />
        <!-- Add your hero image here -->
      </div>
    </div>

    <!-- Features section -->
    <div class="features-section" id="features">
      <h2>Funcionalidades</h2>
      <div class="row flex flex-center feature-cards">
        <div class="col-4 text-center feature-card">
          <q-icon color="primary" name="sym_o_travel_explore" size="50px" />
          <h3>Escolha inteligente</h3>
          <p>Oferecemos duas opções principais para suas jornadas: a busca pela viagem mais confortável e rápida, ou a opção mais econômica.</p>
        </div>
        <div class="col-4 text-center feature-card">
          <q-icon color="primary" name="sym_o_person_play" size="50px" />
          <h3>Fácil Comparação</h3>
          <p>Com apenas alguns cliques, o sistema irá mostrar quais são suas melhores opções de forma simplificada e intuitiva, garantindo uma boa escolha na sua viagem.</p>
        </div>
        <div class="col-4 text-center feature-card">
          <q-icon color="primary" name="sym_o_speed" size="50px" />
          <h3>Desempenho</h3>
          <p>Usamos as últimas tecnologias do mercado, como Django, VueJs e uma API REST para garantir robustez, segurança, rapidez e interfaces intuitivas. Prepare-se para explorar o futuro das viagens com a tecnologia mais avançada ao seu alcance.</p>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
export default {
  methods: {
    scrollToSection(sectionId) {
      const el = document.getElementById(sectionId);
      if (el) {
        el.scrollIntoView({ behavior: "smooth" });
      }
    }
  }
};
</script>

<style scoped>
/* Add your custom styles here */

/* Hero section styles */
.hero-section {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 100px 50px;
}

.hero-content {
  flex: 1;
}

.hero-image {
  flex: 1;
}

/* Features section styles */
.features-section {
  padding: 100px 50px;
}

.feature-cards {
  display: flex;
  justify-content: space-between;
}

.feature-card {
  flex: 1;
  text-align: center;
}

/* Testimonials section styles */
.testimonials-section {
  background-color: #f8f8f8;
  padding: 100px 50px;
}

.testimonial {
  margin-bottom: 50px;
}

/* Footer styles */
.footer {
  background-color: #333;
  color: #fff;
  padding: 20px 50px;
  text-align: center;
}
</style>

