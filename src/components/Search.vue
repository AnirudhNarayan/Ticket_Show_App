<template>
  <div class="search-container">
    <div class="search-header">
      <h2>Search Users</h2>
      <div class="search-box">
        <input type="text" v-model="searchText" placeholder="Search users..." />
        <button @click="searchUsers">Search</button>
      </div>
    </div>
    <div class="search-results">
      <ul>
        <li v-for="user in users" :key="user.id">
          <div class="user-details">
            <h3>{{ user.username }}</h3>
            <p>{{ user.email }}</p>
          </div>
          <div class="user-actions">
            <button v-if="user.followed" @click="unfollowUser(user.id)">
              Unfollow
            </button>
            <button v-else @click="followUser(user.id)">Follow</button>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Search",
  data() {
    return {
      users: [],
      searchText: "",
      token: localStorage.getItem("token"),
    };
  },
  methods: {
    searchUsers() {
      axios
        .get(`http://localhost:7000/search_users?search=${this.searchText}`, {
          headers: {
            token: localStorage.getItem("token"),
            "Access-Control-Allow-Origin": "*",
            "Content-Type": "application/json",
          },
        })
        .then((response) => {
          this.users = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    followUser(userId) {
      axios
        .post(
          `http://localhost:7000/follow/${userId}`,
          {},
          {
            headers: {
              token: localStorage.getItem("token"),
              "Access-Control-Allow-Origin": "*",
              "Content-Type": "application/json",
            },
          }
        )
        .then((response) => {
          // update the followed status of the user in the list
          const userIndex = this.users.findIndex((user) => user.id === userId);
          this.users[userIndex].followed = true;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    unfollowUser(userId) {
      axios
        .post(
          `http://localhost:7000/unfollow/${userId}`,
          {},
          {
            headers: {
              token: localStorage.getItem("token"),
              "Access-Control-Allow-Origin": "*",
              "Content-Type": "application/json",
            },
          }
        )
        .then((response) => {
          // update the followed status of the user in the list
          const userIndex = this.users.findIndex((user) => user.id === userId);
          this.users[userIndex].followed = false;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style>
.search-container {
  margin: 0 auto;
  max-width: 800px;
  padding: 20px;
}

.search-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 20px;
}

.search-box {
  display: flex;
  align-items: center;
}

.search-box input {
  border: none;
  border-bottom: 1px solid #ccc;
  padding: 5px;
  margin-right: 10px;
  font-size: 16px;
  width: 300px;
}

.search-box button {
  border: none;
  background-color: #2196f3;
  color: #fff;
  padding: 10px;
}
</style>