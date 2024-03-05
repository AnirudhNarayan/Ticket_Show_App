<template>
  <div>
    <UserNavbar />
    <div class="theatres-container">
      <div v-for="theatre in theatres" :key="theatre.id" class="theatre-box">
        <h3>{{ theatre.venue_name }}</h3>
        <p>Location: {{ theatre.location }}</p>
        <p>Capacity: {{ theatre.capacity }}</p>
        <button @click="exportToCSV(theatre)">Export CSV</button>
      </div>
    </div>
  </div>
</template>

<script>
import UserNavbar from "@/components/UserNavbar.vue";
import axios from "axios";

export default {
  name: "ExportData",
  components: {
    UserNavbar,
  },
  data() {
    return {
      theatres: [],
    };
  },
  mounted() {
    this.fetchTheatres();
  },
  methods: {
    fetchTheatres() {
      
      axios
        .get("http://localhost:7000/get_display") 
        .then((response) => {
          this.theatres = response.data;
        })
        .catch((error) => {
          console.error("Failed to fetch theatres:", error);
        });
    },
    exportToCSV(theatre) {
      const csvHeader = [
        "Venue Name",
        "Location",
        "Capacity",
        "Ratings",
        "Tags",
        "Timings",
        "Show Names",
      ];
      const csvRows = [csvHeader];

      for (const show of theatre.shows) {
        const csvRow = [
          theatre.venue_name,
          theatre.location,
          theatre.capacity,
          show.ratings,
          show.tags,
          show.timings,
          show.show_name,
        ];
        csvRows.push(csvRow);
      }

      const csvContent = csvRows.map((row) => row.join(",")).join("\n");

      const csvBlob = new Blob([csvContent], {
        type: "text/csv;charset=utf-8;",
      });
      const link = document.createElement("a");
      if (link.download !== undefined) {
        const url = URL.createObjectURL(csvBlob);
        link.setAttribute("href", url);
        link.setAttribute("download", `${theatre.venue_name}_data.csv`);
        link.style.visibility = "hidden";
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
      }
    },
  },
};
</script>

<style>
.theatres-container {
  display: flex;
  flex-wrap: wrap;
}

.theatre-box {
  border: 1px solid #ccc;
  padding: 10px;
  margin: 10px;
  width: 300px;
}
</style>
