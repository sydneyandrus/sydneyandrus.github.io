import { useQuery } from "react-query";
import { Link, NavLink, Navigate, useNavigate, useParams } from "react-router-dom";


function HomePage() {
  return (
    <div>
      <p>come on in!</p>
      <NavLink to="/library">library</NavLink>
      <NavLink to="/diary">diary</NavLink>
      <NavLink to="/about">about</NavLink>
    </div>
  )
}

export default HomePage;