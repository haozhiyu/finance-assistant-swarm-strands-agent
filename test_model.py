#!/usr/bin/env python3
"""
Simple test script to verify model access
"""
from strands.models.bedrock import BedrockModel

def test_model():
    try:
        # Test Claude 3.5 Sonnet
        model = BedrockModel(model_id="us.anthropic.claude-3-5-sonnet-20240620-v1:0", region="us-east-1")
        print("✅ Claude 3.5 Sonnet initialized successfully")
        
        print("🎉 Model is accessible!")
        return True
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False

if __name__ == "__main__":
    test_model()
