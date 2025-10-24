"""
币圈投资助手主入口点
"""

from crypto_assistant.core.agent_core_app import app, BedrockAgentCoreApp


def main():
    """主函数"""
    print("币圈投资助手正在启动...")
    
    # 初始化应用
    crypto_app = BedrockAgentCoreApp()
    crypto_app.setup_agents()
    
    print("系统初始化完成，等待AgentCore调用...")
    
    # 在AgentCore环境中，应用会自动处理请求
    # 这里只是用于本地测试的示例
    test_payload = {
        "session_id": "test_session",
        "query": "请分析比特币的当前市场情况"
    }
    
    result = crypto_app.agent_invocation(test_payload)
    print(f"测试响应: {result}")


if __name__ == "__main__":
    main()