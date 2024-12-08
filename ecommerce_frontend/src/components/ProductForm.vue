<template>
  <div
    class="modal fade"
    id="productModal"
    tabindex="-1"
    aria-labelledby="productModalLabel"
    aria-hidden="true"
  >
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="productModalLabel">
            {{ isEditing ? "Update Product" : "Add Product" }}
          </h5>
          <button
            type="button"
            class="btn-close"
            aria-label="Close"
            @click="closeModal"
          ></button>
        </div>
        <div class="modal-body">
          <form @submit.prevent="validateAndSubmit">
            <div class="mb-3">
              <label for="productName" class="form-label">Name</label>
              <input
                type="text"
                id="productName"
                v-model="product.name"
                class="form-control"
                required
              />
            </div>
            <div class="mb-3">
              <label for="productDescription" class="form-label">Description</label>
              <input
                type="text"
                id="productDescription"
                v-model="product.description"
                class="form-control"
              />
            </div>
            <div class="mb-3">
              <label for="productPrice" class="form-label">Price</label>
              <input
                type="number"
                step="0.01"
                id="productPrice"
                v-model.number="product.price"
                class="form-control"
                :class="{ 'is-invalid': errors.price }"
                required
              />
              <div v-if="errors.price" class="invalid-feedback">
                {{ errors.price }}
              </div>
            </div>
            <div class="mb-3">
              <label for="productStock" class="form-label">Stock</label>
              <input
                type="number"
                id="productStock"
                v-model.number="product.stock"
                class="form-control"
                :class="{ 'is-invalid': errors.stock }"
                required
              />
              <div v-if="errors.stock" class="invalid-feedback">
                {{ errors.stock }}
              </div>
            </div>
            <button type="submit" class="btn btn-primary w-100">
              {{ isEditing ? "Update Product" : "Add Product" }}
            </button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import * as bootstrap from "bootstrap";
export default {
  props: {
    isEditing: Boolean,
    currentProduct: Object,
  },
  data() {
    return {
      product: { ...this.currentProduct },
      errors: {}, // To store validation errors
    };
  },
  methods: {
    validateAndSubmit() {
      this.errors = {}; // Reset errors

      if (this.product.price < 0) {
        this.errors.price = "Price must be a positive value.";
      }
      if (this.product.stock < 0) {
        this.errors.stock = "Stock must be a non-negative value.";
      }

      if (Object.keys(this.errors).length === 0) {
        // No errors, proceed with submission
        this.$emit("formSubmit", this.product);
        this.closeModal();
      }
    },
    closeModal() {
      const modalElement = document.getElementById("productModal");
      const modalInstance = bootstrap.Modal.getInstance(modalElement);
      if (modalInstance) {
        modalInstance.hide();
      }
      this.$emit("closeModal");
    },
  },
  mounted() {
    const modal = new bootstrap.Modal(document.getElementById("productModal"));
    modal.show();
    document
      .getElementById("productModal")
      .addEventListener("hidden.bs.modal", () => {
        this.$emit("closeModal");
      });
  },
};
</script>
