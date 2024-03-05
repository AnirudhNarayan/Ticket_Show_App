import { createRouter, createWebHistory } from 'vue-router';
import Blog from '../components/Blog.vue';
import Register from '../components/Register.vue';
import SignUp from '../components/SignUp.vue';
import NavBar from '../components/NavBar.vue';
import Profile from '../components/Profile.vue';
import Search from '../components/Search.vue';
import DeleteBlog from '../components/DeleteBlog.vue';
import AdminDashboard from '../components/AdminDashboard.vue';
import AdminLogin from '../components/AdminLogin.vue';
import AddTheatre from '../components/AddTheatre.vue';
import Theatre from '../components/Theatre.vue';
import CreateShow from '../components/CreateShow.vue';
import Shows from '../components/Shows.vue';
import EditTheatre from '../components/EditTheatre.vue';
import EditShow from "../components/EditShow.vue";
import UserNavbar from "../components/UserNavbar.vue";
import Display from "../components/Display.vue";
import Book from '../components/Book.vue';
import BookedShows from '../components/BookedShows.vue';
import Export_data from '../components/Export_data.vue'
const routes = [
  {

    component: SignUp,
    name: 'SignUp',
    path: '/'

  },
  {
    path: '/create_show/:id',
    name: 'CreateShow',
    component: CreateShow,
  },
  {
    path: '/booked_shows',
    name: 'BookedShows',
    component: BookedShows,
    props: (route) => ({
      showName: route.query.showName,
      timestamp: route.query.timestamp,
    }),
  },
  
  
  {
    path: '/book/:theaterId/:showId',
    name: 'Book',
    component: Book,
  },
  {
    path: '/display',
    name: 'Display',
    component: Display,
  },
  {
    path: '/export_data',
    name: 'Export_data',
    component: Export_data,
  },
  {
    path: '/user_navbar',
    name: 'UserNavbar',
    component: UserNavbar
  },
  {
    path: '/shows/:id',
    name: 'Shows',
    component: Shows,
  },
  {
    path: '/edit_theatre/:id',
    name: 'EditTheatre',
    component: EditTheatre,
  },

  {
    path: "/edit_show/:showId",
    name: "EditShow",
    component: EditShow,
  },

  {
    component: NavBar,
    name: 'NavBar',
    path: '/navbar'
  },
  {
    component: Theatre,
    name: 'Theatre',
    path: '/theatre'
  },
  {
    component: AddTheatre,
    name: 'AddTheatre',
    path: '/add_theatre'
  },
  {
    component: AdminDashboard,
    name: 'AdminDashboard',
    path: '/admin_dashboard'
  },
  {
    component: Register,
    name: 'Register',
    path: '/register'
  },
  {
    component: Profile,
    name: 'Profile',
    path: '/profile'
  },


  {
    component: Search,
    name: 'search',
    path: '/search'
  },
  {
    component: AdminLogin,
    name: 'AdminLogin',
    path: '/admin_login'
  },
  {
    component: Blog,
    name: 'Blog',
    path: '/blog'
  },
  {
    component: DeleteBlog,
    name: 'DeleteBlog',
    path: '/deleteblog'
  },






];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
