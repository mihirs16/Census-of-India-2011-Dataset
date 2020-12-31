// modules
import React from 'react';

// css
import './header.css';

// assets
import reloadButton from './assets/reload.svg';
import saveButton from './assets/export.svg';


// Small button
class SmallButton extends React.Component {
    render () {
        return (
            <button className="small">
                <img src={this.props.icon} alt=""/>
            </button>
        );
    }
}

// Header
class Header extends React.Component {
    render () {
        return (
        <div className="header">
            <div style={{
                marginLeft: 'auto'
            }}>
                <SmallButton icon={reloadButton}/>
                <SmallButton icon={saveButton}/>
            </div>
        </div>
        );
    }
}

export default Header;
export {
    SmallButton
};