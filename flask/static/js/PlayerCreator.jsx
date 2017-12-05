import React from "react";
import { Panel } from "react-bootstrap";

export default class App extends React.Component {
    render() {
        return (
            <Panel collapsible defaultExpanded header="PG">
                some content here!
            </Panel>
        );
    }
}