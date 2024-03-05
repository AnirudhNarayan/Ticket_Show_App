<template>
  <div>
    <NavBar></NavBar>
    <div class="shows-container">
      <div class="shows">
        <div v-for="show in shows" :key="show.id" class="card mb-2">
          <div class="card-body">
            <h5 class="card-title">{{ show.show_name }}</h5>
            <p class="card-text">
              <em>Tag: {{ show.tags }}</em>
            </p>
            <p class="card-text">
              <em>Ratings: {{ show.ratings }}</em>
            </p>
            <div class="card-buttons">
              <button class="btn btn-info mr-2" @click="editShow(show.id)">
                Edit
              </button>
              <button class="btn btn-danger" @click="deleteShow(show.id)">
                Delete
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import NavBar from './NavBar.vue';

export default {
  name: 'Shows',
  components: {
    NavBar,
  },
  data() {
    return {
      shows: [],
    };
  },
  methods: {
    fetchShows(theatreId) {
      const token = localStorage.getItem('token');

      axios
        .get(`http://localhost:7000/get_shows/${theatreId}`, {
          headers: { Authorization: token },
        })
        .then((response) => {
          this.shows = response.data;
        })
        .catch((error) => {
          console.error('Error fetching shows:', error);
        });
    },
    editShow(id) {
      this.$router.push(`/edit_show/${id}`);
    },
    deleteShow(id) {
      const token = localStorage.getItem('token');

      axios
        .delete(`http://localhost:7000/delete_show/${id}`, {
          headers: { Authorization: token },
        })
        .then((response) => {
          console.log('Show deleted successfully:', response.data);
          this.fetchShows(); 
        })
        .catch((error) => {
          console.error('Error deleting show:', error);
        });
    },
  },
  created() {
    const theatreId = this.$route.params.id;
    this.fetchShows(theatreId);
  },
};
</script>

<style scoped>
.shows-container {
  width: 100%;
  max-width: 2400px;
  margin: 0 auto;
  padding: 200px;
  display: flex;
  justify-content: space-between;
}

.shows {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}

.card {
  max-width: 30rem;
  border: 2px solid #ccc;
  border-radius: 10px;
  padding: 15px;
  margin-bottom: 20px;
  margin-right: 20px; 
  background-color: #fff;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

.card-body {
  padding: 15px;
}

.card-title {
  font-size: 27px;
  font-weight: bold;
  margin-bottom: 10px;
}

.card-buttons {
  display: flex;
  margin-top: 15px;
}

.btn-info {
  background-color: #17a2b8;
  color: #fff;
  font-size: 18px;
  padding: 8px 15px;
  margin-right: 10px; 
}

.btn-danger {
  background-color: #dc3545;
  color: #fff;
  font-size: 18px;
  padding: 8px 15px;
}

.card-text {
  font-style: italic;
}
</style>
