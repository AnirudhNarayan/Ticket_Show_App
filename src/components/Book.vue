<template>
  <div class="book">
    <UserNavbar />
    

    <h2>Available seats: {{ availableSeats }}</h2>
    <h3>Price of each ticket: {{ show.price }}</h3>

    <div class="booking-form">
      <label for="persons">Number of persons:</label>
      <input type="number" id="persons" v-model="numberOfPersons" />
      <button @click="calculateTotal" class="calculate-button">
        Calculate Total
      </button>
    </div>

    <div class="total-section" v-if="totalAmount > 0">
      <h3>Total: {{ totalAmount }}</h3>
      <button @click="confirmBooking" class="confirm-button">
        Confirm Booking
      </button>
    </div>
  </div>
</template>

<script>
import UserNavbar from "./UserNavbar.vue"; 
import axios from "axios";

export default {
  components: {
    UserNavbar, 
  },
  data() {
    return {
      show: {},
      availableSeats: 0,
      numberOfPersons: 0,
      totalAmount: 0,
    };
  },
  created() {
    const theaterId = this.$route.params.theaterId;
    const showId = this.$route.params.showId;
    this.fetchShow(theaterId, showId);
  },
  methods: {
    fetchShow(theaterId, showId) {
      axios
        .get(`http://localhost:7000/get_show/${theaterId}/${showId}`)
        .then((response) => {
          this.show = response.data;
          this.availableSeats = this.show.available_seats;

          // Check if available seats are zero
          if (this.availableSeats === 0) {
            console.log("Housefull");
          }
        })
        .catch((error) => {
          console.error(error);
        });
    },
    calculateTotal() {
      this.totalAmount = this.numberOfPersons * this.show.price;
    },
    confirmBooking() {
      // Check if available seats are greater than the number of persons
      if (this.availableSeats < this.numberOfPersons) {
        console.log("Housefull"); // Display "Housefull" message
        return;
      }

      // Update the available seats on the backend
      const theaterId = this.$route.params.theaterId;
      const showId = this.$route.params.showId;
      const updatedSeats = this.availableSeats - this.numberOfPersons;
      const updateUrl = `http://localhost:7000/update_seats/${theaterId}/${showId}`;
      axios
        .put(updateUrl, { availableSeats: updatedSeats })
        .then((response) => {
          
          console.log("Booking confirmed!");

          // Update the availableSeats value in the component
          this.availableSeats = updatedSeats;

          // Navigate to the bookings page with show name and timestamp as query parameters
          const timestamp = new Date().toISOString();
          this.$router.push({
            name: 'BookedShows',
            query: {
              showName: this.show.show_name,
              timestamp: timestamp,
            },
          });
        })
        .catch((error) => {
          console.error(error);
        });

      // Reset the form
      this.numberOfPersons = 0;
      this.totalAmount = 0;
    },
  },
};
</script>

<style>
.book {
  margin: 20px;
}

.booking-form {
  margin-bottom: 20px;
}

.calculate-button {
  margin-left: 10px;
  padding: 5px 10px;
  cursor: pointer;
}

.total-section {
  margin-top: 20px;
}

.confirm-button {
  background-color: red;
  color: white;
  border: none;
  padding: 5px 10px;
  cursor: pointer;
}

p {
  color: red;
  font-weight: bold;
}
</style>
