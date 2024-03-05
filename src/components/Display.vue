<template>
  <div class="display">
    <UserNavbar />
    <div class="search-bar" style="margin-top: 20px;">
      <input type="text" v-model="searchQuery" placeholder="Search Theater" class="search-input" />
      <input type="text" v-model="locationQuery" placeholder="Location" class="search-input" />
      <input type="number" v-model="ratingQuery" placeholder="Rating" class="search-input" />
      <input type="text" v-model="tagsQuery" placeholder="Tags" class="search-input" />
      <button @click="search" class="search-button">Search</button>
    </div>
    <div class="theater-list">
      <div class="theater-box" v-for="theater in filteredTheaters" :key="theater.id">
        <h2>{{ theater.venue_name }}</h2>
        <p class="details">Location: {{ theater.location }}</p>
        <ul class="show-list">
          <li v-for="show in theater.shows" :key="show.id" class="show">
            <p>{{ show.show_name }} - {{ show.timings }}</p>
            <p class="details">Tags: {{ show.tags }}</p>
            <p class="details">Rating: {{ show.ratings }}</p>
            <button @click="bookTicket(theater.id, show.id)" class="book-button">Book</button>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import UserNavbar from './UserNavbar.vue';

export default {
  components: {
    UserNavbar,
  },
  data() {
    return {
      searchQuery: '',
      locationQuery: '',
      ratingQuery: null,
      tagsQuery: '',
      theaters: [],
    };
  },
  computed: {
    filteredTheaters() {
      return this.theaters.filter((theater) =>
        theater.venue_name.toLowerCase().includes(this.searchQuery.toLowerCase()) &&
        theater.location.toLowerCase().includes(this.locationQuery.toLowerCase()) &&
        (!this.ratingQuery || theater.shows.some((show) => show.ratings === this.ratingQuery)) &&
        theater.shows.some((show) => show.tags.toLowerCase().includes(this.tagsQuery.toLowerCase()))
      );
    },
  },
  mounted() {
    this.fetchTheaters();
  },
  methods: {
    fetchTheaters() {
      axios
        .get('http://localhost:7000/get_display')
        .then((response) => {
          this.theaters = response.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    search() {
      axios
        .get('http://localhost:7000/get_display', {
          params: {
            searchQuery: this.searchQuery,
            locationQuery: this.locationQuery,
            ratingQuery: this.ratingQuery,
            tagsQuery: this.tagsQuery,
          },
        })
        .then((response) => {
          this.theaters = response.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    bookTicket(theaterId, showId) {
      this.$router.push(`/book/${theaterId}/${showId}`);
    },
  },
};
</script>

<style>
.display {
  margin: 20px;
}

.search-bar {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-bottom: 20px;
}

.search-input {
  border: none;
  border-bottom: 1px solid #ccc;
  padding: 10px;
  margin-right: 10px;
  font-size: 18px;
  width: 400px;
}

.search-button {
  border: none;
  background-color: green;
  color: #fff;
  padding: 10px;
  font-size: 16px;
  cursor: pointer;
}

.theater-list {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.theater-box {
  border: 1px solid #ccc;
  padding: 10px;
  margin: 10px;
  width: 400px;
}

.details {
  color: black;
}

.book-button {
  background-color: red;
  color: white;
  border: none;
  padding: 5px 10px;
  margin-top: 10px;
  cursor: pointer;
}
</style>
