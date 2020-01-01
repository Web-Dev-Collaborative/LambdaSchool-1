import React from 'react';
import Profile from './Profile.js';
import TicketListS from './TicketListS.js';
import TicketListH from './TicketListH.js';
import TicketListQ from './TicketListQ.js';

const MainLoad = props => { 
    console.log("Mainload props.profile = " + props.profile);
    if (props.currentUsertype === "helper") {
        return (
            <div>
                <Profile profile={props.profile}/>
                <TicketListH tickets={props.tickets}/>
                <TicketListQ ticketsQ={props.ticketsQ}/>
            </div>
        );

    }
    else {
        return (
            <div>
                <Profile profile={props.profile}/>
                <TicketListS tickets={props.tickets}/>
            </div>
        );
    }

}

export default MainLoad;