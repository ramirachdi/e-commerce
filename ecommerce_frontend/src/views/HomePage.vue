<template>
  <div>
    <ProductForm @product-added="fetchProducts" />
    <ProductList ref="productList" />
  </div>
</template>

<script>
import ProductForm from "@/components/ProductForm.vue";
import ProductList from "@/components/ProductList.vue";

export default {
  components: {
    ProductForm,
    ProductList,
    
  },
  methods: {
    fetchProducts() {
      this.$refs.productList.fetchProducts();
    },
  },
};
</script>
