<template>
  <div>
    <!-- Add Product Button -->
    <div class="d-flex justify-content-between align-items-center mb-3">
      <input
        type="text"
        class="form-control w-50"
        placeholder="Search by name..."
        v-model="searchQuery"
        @input="filterProducts"
      />
      <button class="btn btn-success" @click="showAddModal">Add Product</button>
    </div>

    <!-- Product List -->
    <table class="table table-hover table-bordered">
      <thead class="bg-primary text-white">
        <tr>
          <th>Name</th>
          <th>Description</th>
          <th>Price</th>
          <th>Stock</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="product in paginatedProducts"
          :key="product.id"
          :class="{ 'table-danger': product.stock === 0 }"
        >
          <td>{{ product.name }}</td>
          <td>{{ product.description }}</td>
          <td>${{ parseFloat(product.price).toFixed(2) }}</td>
          <td>{{ product.stock }}</td>
          <td>
            <button
              class="btn btn-sm btn-warning me-2"
              @click="showUpdateModal(product)"
            >
              Update
            </button>
            <button
              class="btn btn-sm btn-danger"
              @click="deleteProduct(product.id)"
            >
              Delete
            </button>
          </td>
        </tr>
      </tbody>
    </table>

    <!-- Pagination -->
    <ProductPagination
      :pageCount="pageCount"
      :currentPage="currentPage"
      @pageChanged="handlePageClick"
    />

    <!-- Conditionally Render Product Form Modal -->
    <ProductForm
      v-if="showModal"
      :isEditing="isEditing"
      :currentProduct="currentProduct"
      @formSubmit="handleFormSubmit"
      @closeModal="closeModal"
    />
  </div>
</template>

<script>
import api from "@/services/api";
import ProductForm from "./ProductForm.vue";
import ProductPagination from "./ProductPagination.vue";

export default {
  components: {
    ProductForm,
    ProductPagination,
  },
  data() {
    return {
      products: [],
      filteredProducts: [],
      currentPage: 1,
      isEditing: false,
      currentProduct: {
        id: null,
        name: "",
        description: "",
        price: 0.0,
        stock: 0,
      },
      searchQuery: "", // Holds the user's search input
      showModal: false,
    };
  },
  computed: {
    pageCount() {
      return Math.ceil(this.filteredProducts.length / 5);
    },
    paginatedProducts() {
      const start = (this.currentPage - 1) * 5;
      return this.filteredProducts.slice(start, start + 5);
    },
  },
  methods: {
    fetchProducts() {
      api.getProducts().then((response) => {
        this.products = response.data;
        this.filteredProducts = [...this.products];
      });
    },
    handlePageClick(page) {
      this.currentPage = page;
    },
    deleteProduct(id) {
      api.deleteProduct(id).then(() => {
        this.fetchProducts();
      });
    },
    showAddModal() {
      this.isEditing = false;
      this.currentProduct = { id: null, name: "", description: "", price: 0.0, stock: 0 };
      this.showModal = true;
    },
    showUpdateModal(product) {
      this.isEditing = true;
      this.currentProduct = { ...product };
      this.showModal = true;
    },
    closeModal() {
      this.showModal = false;
    },
    handleFormSubmit(product) {
      if (this.isEditing) {
        api.updateProduct(product.id, product).then(() => {
          this.fetchProducts();
          this.closeModal();
        });
      } else {
        api.addProduct(product).then(() => {
          this.fetchProducts();
          this.closeModal();
        });
      }
    },
    filterProducts() {
      const query = this.searchQuery.toLowerCase();
      this.filteredProducts = this.products.filter((product) =>
        product.name.toLowerCase().includes(query)
      );
      this.currentPage = 1; // Reset to the first page after filtering
    },
  },
  created() {
    this.fetchProducts();
  },
};
</script>


<style>
.table-danger {
  background-color: #f8d7da !important;
  color: #721c24 !important;
}

.table-hover tbody tr:hover {
  background-color: #f5f5f5;
}

button {
  border-radius: 6px;
}
</style>
