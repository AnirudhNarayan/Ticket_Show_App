<template>
  <div class="profile-container">
    <div class="profile-header">
      <h2>Profile</h2>
      <div class="profile-stats">
        <div class="followers">
          <h3>{{ followers }}</h3>
          <p>Followers</p>
        </div>

        <div class="following">
          <h3>{{ following }}</h3>
          <p>Following</p>
        </div>
      </div>
    </div>
    <div class="blog-container">
      <h3>Blogs</h3>
      <div v-for="blog in blogs" :key="blog.blog_id" class="blog-card">
        <div class="blog-image">
          <img
            :src="'http://127.0.0.1:7000/uploads/' + blog.image_path"
            alt="Blog Image"
          />
        </div>
        <div class="blog-details">
          <h4>{{ blog.title }}</h4>
          <p>{{ blog.description }}</p>
          <router-link to="/blog">
          <button>Edit</button>
          </router-link>
          <br>
          <br>
          <button @click="deleteBlog(blog.blog_id)">Delete</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  
  data() {
    return {
      followers: 0,
      following: 0,
      blogs: [],
      imagesrc: "",
    };
  },
  mounted() {
    axios
      .get("http://localhost:7000/get_blogs", {
        headers: {
          token: localStorage.getItem("token"),
          "Access-Control-Allow-Origin": "*",
          "Content-Type": "application/json",
        },
      })
      .then((response) => {
        this.followers = response.data.followers;
        this.following = response.data.following;
        this.blogs = response.data.blogs;
        this.imagesrc = response.data.blog.image_path;
      })
      .catch((error) => {
        console.log(error);
      });
  },


methods: {
    deleteBlog(blog_id) {
      axios
        .delete(`http://localhost:7000/delete_blog/${blog_id}`, {
          headers: {
            token: localStorage.getItem("token"),
            "Access-Control-Allow-Origin": "*",
            "Content-Type": "application/json",
          },
        })
        .then((response) => {
          console.log(response);
          this.blogs = this.blogs.filter((blog) => blog.blog_id !== blog_id);
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },




};
</script>

<style>
.profile-container {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  box-sizing: border-box;
}

.profile-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.profile-stats {
  display: flex;
}

.followers,
.following {
  margin-right: 20px;
}

.blog-container {
  margin-top: 20px;
}

.blog-card {
  display: flex;
  margin-bottom: 20px;
  padding: 20px;
  background-color: #f5f5f5;
  border-radius: 5px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.blog-image {
  width: 200px;
  height: 200px;
  margin-right: 20px;
}

.blog-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.blog-details {
  flex-grow: 1;
}

.blog-details h4 {
  margin-top: 0;
  margin-bottom: 10px;
}

.blog-details p {
  margin-top: 0;
  font-size: 16px;
  line-height: 1.5;
}
</style>
