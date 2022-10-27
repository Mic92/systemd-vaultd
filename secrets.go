package main

import (
	"encoding/json"
	"fmt"
	"os"
)

func parseServiceSecrets(path string) (map[string]interface{}, error) {
	content, err := os.ReadFile(path)
	if err != nil {
		return nil, fmt.Errorf("Cannot read json file '%s': %w", path, err)
	}
	var data map[string]interface{}
	err = json.Unmarshal(content, &data)
	if err != nil {
		return nil, fmt.Errorf("Cannot parse '%s' as json file: %w", path, err)
	}
	return data, nil
}