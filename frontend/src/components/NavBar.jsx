import { NavLink } from "react-router-dom";

function NavItem({ to, name, right }) {
  const className = [
    "text-center font-bold mx-4",
    "py-2 px-4",
    "hover:text-teal-600",
    right ? "border-0" : "border-0"
  ].join(" ")

  const getClassName = ({ isActive }) => (
    isActive ? className + " text-cyan-700" : className
  );

  return (
    <NavLink to={to} className={getClassName}>
      {name}
    </NavLink>
  );
}

function NavBar() {
  return (
    <nav className="flex flex-row mt-4 mx-4 text-teal-800 text-xl">
      <NavItem to="/" name="sydney andrus" />
      <div className="flex-1" />
      <NavItem to="/library" name="library" />
      <NavItem to="/diary" name="diary" />
      <NavItem to="/about" name="about" />
    </nav>
  );
}

export default NavBar;