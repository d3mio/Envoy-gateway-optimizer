package main

import (
	"context"
	"encoding/json"
	"flag"
	"fmt"
	"log"
	"os"
	"path/filepath"
	"strings"
	"time"

	"github.com/envoyproxy/go-control-plane/envoy/config/core/v3"
	"github.com/envoyproxy/go-control-plane/envoy/config/listener/v3"
	"github.com/envoyproxy/go-control-plane/envoy/config/route/v3"
	"github.com/envoyproxy/go-control-plane/envoy/type/v3"
	"github.com/envoyproxy/go-control-plane/pkg/wrapped"
	"google.golang.org/protobuf/types/known/anypb"
	"google.golang.org/protobuf/types/known/wrapperspb"
)

const (
	defaultConfigFile = "config.yaml"
	defaultEnvoyConfig = "envoy.yaml"
)

var (
	configFile string
	envoyConfig string
	verbose bool
)

func init() {
	flag.StringVar(&configFile, "config", defaultConfigFile, "Path to the configuration file")
	flag.StringVar(&envoyConfig, "envoy", defaultEnvoyConfig, "Path to the Envoy configuration file")
	flag.BoolVar(&verbose, "verbose", false, "Enable verbose logging")
}

func main() {
	flag.Parse()

	// Load configuration from file
	config, err := loadConfig(configFile)
	if err != nil {
		log.Fatal(err)
	}

	// Create Envoy configuration
	envoyCfg, err := createEnvoyConfig(config)
	if err != nil {
		log.Fatal(err)
	}

	// Write Envoy configuration to file
	if err := writeEnvoyConfig(envoyCfg, envoyConfig); err != nil {
		log.Fatal(err)
	}

	log.Println("Envoy configuration generated successfully")
}

func loadConfig(file string) (*Config, error) {
	data, err := os.ReadFile(file)
	if err != nil {
		return nil, err
	}

	var config Config
	if err := json.Unmarshal(data, &config); err != nil {
		return nil, err
	}

	return &config, nil
}

func createEnvoyConfig(config *Config) (*v3.Listener, error) {
	listener := &v3.Listener{
		Name: "enterprise-service-mesh",
		Address: &v3.Address{
			Address: &v3.Address_SocketAddress{
				SocketAddress: &v3.SocketAddress{
					Address: "0.0.0.0",
					PortValue: 8080,
				}
			}
		},
	}

	// Create filter chain
	filterChain := &v3.FilterChain{
		Filters: []*v3.Filter{
			{
				Name: "envoy.http_connection_manager",
				TypedConfig: &anypb.Any{
					TypeUrl: "type.googleapis.com/envoy.config.filter.http.connection_manager.v3.HttpConnectionManager",
					Value: wrapped.Marshal(&v3.HttpConnectionManager{
						StatPrefix: "http",
						RouteConfig: &v3.RouteConfiguration{
							Name: "local_route",
							VirtualHosts: []*v3.VirtualHost{
								{
									Name: "*",
									Domains: []string{"*"},
									Routes: []*v3.Route{
										{
											Match: &v3.RouteMatch{
												Prefix: "/",
											},
											Action: &v3.Route_Route{
												Cluster: "local_service",
											},
									}
								},
						}
						},
					}
				})},
			}
		},
		}
	}

	listener.FilterChains = append(listener.FilterChains, filterChain)

	return listener, nil
}

func writeEnvoyConfig(cfg *v3.Listener, file string) error {
	data, err := wrapped.Marshal(cfg)
	if err != nil {
		return err
	}

	if err := os.WriteFile(file, data, 0644); err != nil {
		return err
	}

	return nil
}

// Config represents the configuration for the Enterprise Service Mesh Performance Optimizer
type Config struct {
	Clusters []Cluster `json:"clusters"`
}

// Cluster represents a cluster in the configuration
-type Cluster struct {
	Name string `json:"name"`
}
