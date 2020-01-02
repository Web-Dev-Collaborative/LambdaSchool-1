import React, { useState, useEffect } from "react";
import hideLogin, { hideSignup } from "./Hide";
import { Link } from 'react-router-dom';
import TicketH from './TicketH.js';

// import Ticket from '../components/Ticket.js';
    
    // TODO: 3 Not only are standard network request techniques employed, the code is organized in such a fashion that the student demonstrated proper use of container vs presentational components or other industry standards, conventions or patterns.
  
	  // TODO: 3 Student showed great insight in setting up the state management for the app's forms. 
	  // TODO: 2 proper usage of state and props are demonstrated throughout the project
    // TODO: 2 proper usage of useState and useEffect hooks are clearly incorporated and correctly implemented. 
  
    // TODO: 3 Student went above and beyond the project (search function?)
    // TODO: 3 Student incorporated a third party event/animation library like unto Greensock, Anime, React-motion etc.
    // TODO: 2 Student used Array methods to dynamically render HTML elements.
	  // TODO: 3 Loading states and success/error notifications are in place and add to the overall UX of the app.
    // TODO: 3 Student used advanced React techniques like the composition pattern, custom hooks, render props, HOCs, etc.
    
    // TODO: 3 Student was able to architect components to be easily reused. 
	  // TODO: 2 Student created functional components and used events in application to add dynamic functionality to app.
	  // TODO: 2 the UI is composed of small reusable components
	  // TODO: 2 Student's code was organized at the component level
    // TODO: 2 Student has set up component management for the forms in the app that makes sense for each form. 

// hide current page when login showing
hideLogin();
// hide current page when sign-up showing
hideSignup();

const SearchForm = props => {
  const [searchTerm, setSearchTerm] = useState("");
  const [searchResults, setSearchResults] = useState([]);


  useEffect(() => {
    if (props.tickets != null) {
      const results = props.tickets.filter(ticket =>
        ticket.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
        ticket.status.toLowerCase().includes(searchTerm.toLowerCase()) ||
        ticket.description.toLowerCase().includes(searchTerm.toLowerCase()) ||
        ticket.category.toLowerCase().includes(searchTerm.toLowerCase())  ||
        ticket.date.toLowerCase().includes(searchTerm.toLowerCase()) 
      );
      console.log("useEffect Search Results = " + results);
      setSearchResults([...results]);
    }
  }, [searchTerm, props.tickets]);

  const handleChange = event => {
    setSearchTerm(event.target.value);
  };

  return (
    <section className="search-form">
      <h1>Your Tickets:  </h1>
      <form>
        <label htmlFor="name">Search:</label>
        <input
          id="name"
          type="text"
          name="textfield"
          placeholder="Search"
          value={searchTerm}
          onChange={handleChange}
        />
        {
          searchResults.map(
            ticket => (
              <Link to="/ticket"><TicketH key={ticket.id} ticket={ticket} /></Link>
            )
          )
        }
      </form>
    </section>
    
  );
}

export default SearchForm;