// modules
import React from 'react';

// css
import './sidebar.css';

// Menu Option Button
class OptionButton extends React.Component {
    render () {
        return (
            <div>
                <input type="radio" name={this.props.group} id={this.props.text} defaultChecked={this.props.checked}/>
                <label htmlFor={this.props.text}>{this.props.text}</label>
            </div>
        );
    }
}

// Sidebar
class Sidebar extends React.Component {
    render () {
        return (
            <div className="sidebar">
                <OptionButton group="Menu" text="Home" checked={true}/>
                <OptionButton group="Menu" text="State" />
                <OptionButton group="Menu" text="District" />
                <OptionButton group="Menu" text="Delivery" />
                <OptionButton group="Menu" text="About Us" />
            </div>
        );
    }
}

export default Sidebar;