import React, { Component } from "react";
import axios from "axios";

class AllTeams extends Component {

    constructor(props) {
        super(props)
        this.state = {
            data: [],
            isLoading: true,
        };
    }


    componentDidMount = () => {
        axios.get('http://localhost:5000/teams')
        .then(res => {
            this.setState({data: res.data})
            console.log(res)
        })
        .catch((e) => {
            console.log(e)
        });

        this.setState({isLoading: false})
    }

    displayTeams = () => {

        if (!this.state.data) {

            let empty_header = React.createElement("h1", {className: "empty_header"}, "Error, no teams found.");
            return empty_header;
        }
        else {
            let list_items = [];

            for (const key of Object.keys(this.state.data)) {

                let teams_arr = this.state.data[key]

                teams_arr.forEach( team => {
                    let url = "teams/" + team.team_id;
    
                    let a = (
                        <li><a href={url}>{team.team_name}</a></li>
                    );
    
                    list_items.push(a);
                });
            }

            let element = (
                <ul>{list_items}</ul>
            );

            return element;

        }
    }

    render() {
        return (
            <div>
                {this.displayTeams()}
            </div>
        )
    }
}

export default AllTeams
