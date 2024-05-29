import React from "react";
import { NavLink, useLocation } from "react-router-dom";
import { Nav } from "reactstrap";
import PerfectScrollbar from "perfect-scrollbar";

var ps;

function Sidebar(props) {
    const location = useLocation();
    const sidebar = React.useRef();
    
    const activeRoute = (routeName) => {
        return location.pathname.indexOf(routeName) > -1 ? "active" : "";
    };

    React.useEffect(() => {
        if (navigator.userAgent.indexOf("Win") > -1) {
            ps = new PerfectScrollbar(sidebar.current, {
                suppressScrollX: true,
                suppressScrollY: false,
            });
        }
        return function cleanup() {
            if (navigator.userAgent.indexOf("Win") > -1) {
                ps.destroy();
            }
        };
    });

    if (!props.routes || !Array.isArray(props.routes)) {
        return null;
    }

    return (
        <div
            className="sidebar"
            data-color={props.bgColor}
            data-active-color={props.activeColor}
        >
            {/* Your existing JSX code */}
            <div className="sidebar-wrapper" ref={sidebar}>
                <Nav>
                    {props.routes.map((prop, key) => (
                        <li
                            className={
                                activeRoute(prop.path) + (prop.pro ? " active-pro" : "")
                            }
                            key={key}
                        >
                            <NavLink to={prop.layout + prop.path} className="nav-NavLink">
                                <i className={prop.icon} />
                                <p>{prop.name}</p>
                            </NavLink>
                        </li>
                    ))}
                </Nav>
            </div>
        </div>
    );
}

export default Sidebar;







