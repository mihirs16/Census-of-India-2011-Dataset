// modules
import React from 'react';
import Plotly from "plotly.js-mapbox-dist";
import createPlotlyComponent from "react-plotly.js/factory";

// css
import './dashboard.css';

// geojson file
import states_india from './states_india.json';
// import districts_india from './districts_india.json';

const Plot = createPlotlyComponent(Plotly);

// Map plot
class MapPlot extends React.Component {

    makeList(num, num_start=0) {
        let arr = [];
        for (let i = num_start; i < num; i++) {
            arr.push(i);
        }
        return arr;
    }

    render () {
        return (
            <Plot
                style = {{
                    height: '100%',
                    width: '100%'
                }}
                data = {[{
                    type: "choroplethmapbox",
                    geojson: states_india,
                    locations: this.makeList(36), 
                    z: this.makeList(72, 36),
                    featureidkey: 'properties.state_code',
                    hoverinfo: 'properties.st_nm',
                    coloraxis: 'coloraxis'
                }]}

                layout = {{
                    autosize: true,
                    mapbox: {
                        center: {
                            lon: 78, 
                            lat: 22.5
                        }, 
                        zoom: 4.25,
                        style: 'dark',
                    },
                    margin: {
                        l: 0,
                        r: 0,
                        t: 0,
                        b: 0
                    },
                    coloraxis: {
                        showscale: false
                    }
                }}

                config = {{
                    mapboxAccessToken: "pk.eyJ1IjoibWloaXJzMTYiLCJhIjoiY2tiMGRobjBoMDdrZDJ3c2R6YndyOW51NCJ9.O-dhJlZXKBK78AbTjngkFw",
                    displayModeBar: false
                }}
                useResizeHandler = {true}

            />
        );
    }
}

// Dashboard
class Dashboard extends React.Component {
    render () {
        return (
            <div className="dashboard">
                <MapPlot />
            </div>
        );
    }
}

export default Dashboard;