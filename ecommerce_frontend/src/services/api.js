import axios from "axios";

const apiClient = axios.create({
    baseURL: "http://127.0.0.1:8000/api", // Your Django API URL
    headers: {
        "Content-Type": "application/json",
    },
});

export default {
    getProducts() {
        return apiClient.get("/products/");
    },
    addProduct(product) {
        return apiClient.post("/products/", product);
    },
    updateProduct(id, product) {
        return apiClient.put(`/products/${id}/`, product);
    },
    deleteProduct(id) {
        return apiClient.delete(`/products/${id}/`);
    },
};
