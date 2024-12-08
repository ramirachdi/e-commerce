<template>
  <div id="app" class="container mt-5">
    <header class="text-center mb-4">
      <h1 class="text-primary">E-commerce Product Management</h1>
    </header>
    <main>
      <!-- Product List -->
      <div class="card shadow">
        <div class="card-header bg-secondary text-white text-center">Product List</div>
        <div class="card-body">
          <ProductList :page-size="5" />
        </div>
      </div>
    </main>
  </div>
</template>

<script>
import ProductList from "./components/ProductList.vue";

export default {
  name: "App",
  components: {
    ProductList,
  },
};
</script>

<style>
body {
  background-color: #f8f9fa;
  font-family: "Roboto", sans-serif;
}

#app {
  max-width: 1200px;
  margin: 0 auto;
}

.card {
  border-radius: 12px;
}

.card-body {
  padding: 20px;
}

button {
  border-radius: 8px;
}
</style>
