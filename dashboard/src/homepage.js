// modules
import React from 'react';

// components
import Header from './components/header';
import Sidebar from './components/sidebar';
import Dashboard from './components/dashboard';

// Homepage 
class Homepage extends React.Component {
    render () {
        return (
            <div className="homepage">
                <Header />
                <div className="content" style={{
                    display: 'flex',
                }}>
                    <Sidebar />
                    <Dashboard />
                </div>
            </div> 
        );       
    }
}

export default Homepage;