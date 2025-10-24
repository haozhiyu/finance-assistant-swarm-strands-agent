#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简单的任务管理器
功能：添加任务、查看任务、标记完成、删除任务
"""

import json
import os
from datetime import datetime

class TaskManager:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self.load_tasks()
    
    def load_tasks(self):
        """从文件加载任务"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except (json.JSONDecodeError, FileNotFoundError):
                return []
        return []
    
    def save_tasks(self):
        """保存任务到文件"""
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(self.tasks, f, ensure_ascii=False, indent=2)
    
    def add_task(self, description):
        """添加新任务"""
        task = {
            'id': len(self.tasks) + 1,
            'description': description,
            'completed': False,
            'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        self.tasks.append(task)
        self.save_tasks()
        print(f"✅ 任务已添加: {description}")
    
    def view_tasks(self):
        """查看所有任务"""
        if not self.tasks:
            print("📝 暂无任务")
            return
        
        print("\n📋 任务列表:")
        print("-" * 50)
        for task in self.tasks:
            status = "✅" if task['completed'] else "⏳"
            print(f"{status} [{task['id']}] {task['description']}")
            print(f"    创建时间: {task['created_at']}")
        print("-" * 50)
    
    def complete_task(self, task_id):
        """标记任务为完成"""
        for task in self.tasks:
            if task['id'] == task_id:
                task['completed'] = True
                task['completed_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                self.save_tasks()
                print(f"🎉 任务已完成: {task['description']}")
                return
        print(f"❌ 未找到ID为 {task_id} 的任务")
    
    def delete_task(self, task_id):
        """删除任务"""
        for i, task in enumerate(self.tasks):
            if task['id'] == task_id:
                deleted_task = self.tasks.pop(i)
                self.save_tasks()
                print(f"🗑️  任务已删除: {deleted_task['description']}")
                return
        print(f"❌ 未找到ID为 {task_id} 的任务")
    
    def show_statistics(self):
        """显示任务统计"""
        total = len(self.tasks)
        completed = sum(1 for task in self.tasks if task['completed'])
        pending = total - completed
        
        print(f"\n📊 任务统计:")
        print(f"总任务数: {total}")
        print(f"已完成: {completed}")
        print(f"待完成: {pending}")
        if total > 0:
            completion_rate = (completed / total) * 100
            print(f"完成率: {completion_rate:.1f}%")

def main():
    """主程序"""
    manager = TaskManager()
    
    print("🎯 欢迎使用任务管理器!")
    print("输入 'help' 查看帮助信息")
    
    while True:
        try:
            command = input("\n请输入命令: ").strip().lower()
            
            if command == 'help' or command == 'h':
                print("""
📖 可用命令:
- add <任务描述>     : 添加新任务
- list 或 ls        : 查看所有任务
- complete <任务ID> : 标记任务为完成
- delete <任务ID>   : 删除任务
- stats             : 查看任务统计
- help 或 h         : 显示帮助信息
- quit 或 q         : 退出程序
                """)
            
            elif command.startswith('add '):
                description = command[4:].strip()
                if description:
                    manager.add_task(description)
                else:
                    print("❌ 请输入任务描述")
            
            elif command in ['list', 'ls']:
                manager.view_tasks()
            
            elif command.startswith('complete '):
                try:
                    task_id = int(command[9:].strip())
                    manager.complete_task(task_id)
                except ValueError:
                    print("❌ 请输入有效的任务ID")
            
            elif command.startswith('delete '):
                try:
                    task_id = int(command[7:].strip())
                    manager.delete_task(task_id)
                except ValueError:
                    print("❌ 请输入有效的任务ID")
            
            elif command == 'stats':
                manager.show_statistics()
            
            elif command in ['quit', 'q']:
                print("👋 再见!")
                break
            
            else:
                print("❌ 未知命令，输入 'help' 查看帮助")
        
        except KeyboardInterrupt:
            print("\n👋 程序已退出")
            break
        except Exception as e:
            print(f"❌ 发生错误: {e}")

if __name__ == "__main__":
    main()