<template>
  <div class="booked-shows">
    <UserNavbar />

    <div class="booking-details">
      <h1>Booking Details</h1>
      <div class="box">
        <p>Show Name: {{ $route.query.showName }}</p>
        <p>Timestamp: {{ formatTimestamp($route.query.timestamp) }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import UserNavbar from "./UserNavbar.vue"; 

export default {
  name: 'BookedShows',
  components: {
    UserNavbar,
  },
  methods: {
    formatTimestamp(timestamp) {
      const date = new Date(timestamp);
      const formattedDate = date.toLocaleDateString();
      const formattedTime = date.toLocaleTimeString();
      return `${formattedDate} ${formattedTime}`;
    },
  },
};
</script>

<style scoped>
.booked-shows {
  margin: 20px;
}

.booking-details {
  border: 1px solid #080808;
  padding: 20px;
}

.box {
  margin-bottom: 10px;
}
</style>
