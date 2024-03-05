<template>
  <div class="theatre-container">
    <div class="theatres">
      <div v-for="theatre in theatres" :key="theatre.id" class="card mb-2">
        <div class="card-body">
          <h5 class="card-title">{{ theatre.venueName }}</h5>
          <p class="card-text">{{ theatre.location }}</p>
          <p class="card-text">Capacity: {{ theatre.capacity }}</p>
          <!-- Add other theatre details as needed -->
          <div class="card-buttons">
            <button class="btn btn-info mr-2" @click="editTheatre(theatre.id)">
              Edit
            </button>
            <button
              class="btn btn-danger mr-2"
              @click="deleteTheatre(theatre.id)"
            >
              Delete
            </button>
            <button class="btn btn-primary" @click="goToCreateShow(theatre.id)">
              +
            </button>
            <button class="btn btn-secondary" @click="viewShows(theatre.id)">
              View Shows
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Theatre",
  data() {
    return {
      theatres: [],
    };
  },
  methods: {
    fetchTheatres() {
      const token = localStorage.getItem("token");

      axios
        .get("http://localhost:7000/get_theatres", {
          headers: { Authorization: token },
        })
        .then((response) => {
          this.theatres = response.data;
        })
        .catch((error) => {
          console.error("Error fetching theatres:", error);
        });
    },
    editTheatre(id) {
      // Logic to edit a specific theatre using the id
      this.$router.push(`/edit_theatre/${id}`);
    },
    deleteTheatre(id) {
      const token = localStorage.getItem("token");

      axios
        .delete(`http://localhost:7000/delete_theatre/${id}`, {
          headers: {
            Authorization: token,
          },
        })
        .then((response) => {
          console.log("Theatre deleted successfully");
          this.fetchTheatres();
        })
        .catch((error) => {
          console.error("Error deleting theatre:", error);
        });
    },

    goToCreateShow(id) {
      this.$router.push(`/create_show/${id}`);
    },
    viewShows(id) {
      this.$router.push(`/shows/${id}`);
    },
  },
  created() {
    this.fetchTheatres();
  },
};
</script>
<style scoped>
.theatre-container {
  width: 100%;
  max-width: 2400px;
  margin: 0 auto;
  padding: 200px;
  display: flex;
  justify-content: space-between;
}

.theatres {
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

.card-text {
  margin-bottom: 10px;
}

.card-buttons {
  display: flex;
  flex-direction: column;
  margin-top: 15px;
}

.btn-primary {
  background-color: #007bff;
  color: #fff;
  font-size: 18px;
  padding: 8px 15px;
  margin-bottom: 10px; 
}
.btn-secondary {
  background-color: #ff00bb;
  color: #fff;
  font-size: 18px;
  padding: 8px 15px;
  margin-bottom: 10px; 
}

.btn-danger {
  background-color: #dc3545;
  color: #fff;
  font-size: 18px;
  padding: 8px 15px;
  margin-bottom: 10px; 
}

.btn-info {
  background-color: #17a2b8;
  color: #fff;
  font-size: 18px;
  padding: 8px 15px;
  margin-bottom: 10px; 
}

.add-theatre {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background-color: #007bff;
  color: white;
  width: 75px;
  height: 75px;
  border-radius: 50%;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
  font-size: 36px;
}
</style>
