import { createApp } from 'vue';
import App from './App.vue';
import router from './router'; // Import the router
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap";
import "bootstrap/dist/css/bootstrap.min.css"; // Bootstrap CSS
import "bootstrap/dist/js/bootstrap.bundle.min.js"; // Bootstrap JavaScript


const app = createApp(App);

app.use(router); // Register the router
app.mount('#app');
