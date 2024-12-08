<template>
    <div class="d-flex justify-content-between align-items-center mt-3">
      <button
        class="btn btn-outline-primary"
        :disabled="currentPage === 1"
        @click="changePage(currentPage - 1)"
      >
        Previous
      </button>
  
      <div>
        <button
          v-for="page in pageCount"
          :key="page"
          :class="['btn', page === currentPage ? 'btn-primary' : 'btn-outline-secondary', 'mx-1']"
          @click="changePage(page)"
        >
          {{ page }}
        </button>
      </div>
  
      <button
        class="btn btn-outline-primary"
        :disabled="currentPage === pageCount"
        @click="changePage(currentPage + 1)"
      >
        Next
      </button>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      pageCount: Number,
      currentPage: Number,
    },
    methods: {
      changePage(page) {
        this.$emit("pageChanged", page);
      },
    },
  };
  </script>
  