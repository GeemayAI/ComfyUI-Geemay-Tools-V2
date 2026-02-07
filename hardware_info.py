# -*- coding: utf-8 -*-
"""
硬件信息采集模块
用于获取主板UUID、CPU ID、MAC地址等硬件唯一标识
支持 Windows、Linux、macOS 系统
"""

import subprocess
import platform
import hashlib
import uuid


def get_board_uuid():
    """
    获取主板UUID（真实的主板序列号）
    返回：
        主板UUID字符串（已标准化：去空格、转大写）
    """
    try:
        system = platform.system()
        
        if system == "Windows":
            # 方案1：使用 wmic（Windows 10 优先，兼容性最好）
            try:
                result = subprocess.check_output(
                    "wmic csproduct get uuid",
                    shell=True,
                    stderr=subprocess.DEVNULL,
                    timeout=10,
                    encoding='gbk',  # Windows 中文系统使用 gbk 编码
                    errors='ignore'
                )
                
                # 解析输出（第一行是标题，第二行是UUID）
                lines = [line.strip() for line in result.split('\n') if line.strip()]
                if len(lines) >= 2 and lines[1] != 'UUID':
                    board_uuid = lines[1].strip().upper()
                    if board_uuid and board_uuid != "":
                        return board_uuid
            except Exception as e:
                print(f"wmic 获取主板UUID失败: {e}")
            
            # 方案2：使用 PowerShell（Windows 11 兼容）
            try:
                result = subprocess.check_output(
                    'powershell -Command "Get-CimInstance -ClassName Win32_ComputerSystemProduct | Select-Object -ExpandProperty UUID"',
                    shell=True,
                    stderr=subprocess.DEVNULL,
                    timeout=10,
                    encoding='utf-8',
                    errors='ignore'
                )
                
                board_uuid = result.strip().upper()
                if board_uuid and board_uuid != "":
                    return board_uuid
            except Exception as e:
                print(f"PowerShell 获取主板UUID失败: {e}")
            
            # 方案3：使用注册表（最后备用方案）
            try:
                import winreg
                key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\HardwareConfig")
                board_uuid, _ = winreg.QueryValueEx(key, "LastConfig")
                winreg.CloseKey(key)
                if board_uuid:
                    return board_uuid.upper()
            except Exception as e:
                print(f"注册表获取主板UUID失败: {e}")
            
        elif system == "Linux":
            # Linux: 读取 /sys/class/dmi/id/product_uuid
            try:
                with open('/sys/class/dmi/id/product_uuid', 'r') as f:
                    board_uuid = f.read().strip().upper()
                    return board_uuid
            except:
                # 备用方案：使用 dmidecode
                result = subprocess.check_output(
                    "sudo dmidecode -s system-uuid",
                    shell=True,
                    stderr=subprocess.DEVNULL
                ).decode('utf-8', errors='ignore')
                board_uuid = result.strip().upper()
                return board_uuid
                
        elif system == "Darwin":  # macOS
            # macOS: 使用 system_profiler 获取硬件UUID
            result = subprocess.check_output(
                "system_profiler SPHardwareDataType | grep 'Hardware UUID'",
                shell=True,
                stderr=subprocess.DEVNULL
            ).decode('utf-8', errors='ignore')
            
            # 解析输出：Hardware UUID: XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
            if "Hardware UUID:" in result:
                board_uuid = result.split("Hardware UUID:")[1].strip().upper()
                return board_uuid
        
        # 如果所有方法都失败，返回默认值
        return "UNKNOWN_BOARD_UUID"
        
    except Exception as e:
        print(f"获取主板UUID失败: {e}")
        return "UNKNOWN_BOARD_UUID"


def get_cpu_id():
    """
    获取CPU ID（唯一的CPU序列号）
    返回：
        CPU ID字符串（已标准化：去空格、转大写）
    """
    try:
        system = platform.system()
        
        if system == "Windows":
            # 方案1：使用 wmic（Windows 10 优先，兼容性最好）
            try:
                result = subprocess.check_output(
                    "wmic cpu get processorid",
                    shell=True,
                    stderr=subprocess.DEVNULL,
                    timeout=10,
                    encoding='gbk',  # Windows 中文系统使用 gbk 编码
                    errors='ignore'
                )
                
                # 解析输出（第一行是标题，第二行是ProcessorId）
                lines = [line.strip() for line in result.split('\n') if line.strip()]
                if len(lines) >= 2 and lines[1] != 'ProcessorId':
                    cpu_id = lines[1].strip().upper()
                    if cpu_id and cpu_id != "":
                        return cpu_id
            except Exception as e:
                print(f"wmic 获取CPU ID失败: {e}")
            
            # 方案2：使用 PowerShell（Windows 11 兼容）
            try:
                result = subprocess.check_output(
                    'powershell -Command "Get-CimInstance -ClassName Win32_Processor | Select-Object -ExpandProperty ProcessorId"',
                    shell=True,
                    stderr=subprocess.DEVNULL,
                    timeout=10,
                    encoding='utf-8',
                    errors='ignore'
                )
                
                cpu_id = result.strip().upper()
                if cpu_id and cpu_id != "":
                    return cpu_id
            except Exception as e:
                print(f"PowerShell 获取CPU ID失败: {e}")
            
        elif system == "Linux":
            # Linux: 读取 /proc/cpuinfo 中的序列号
            try:
                with open('/proc/cpuinfo', 'r') as f:
                    for line in f:
                        if 'Serial' in line or 'serial' in line:
                            cpu_id = line.split(':')[1].strip().upper()
                            return cpu_id
            except:
                pass
            
            # 备用方案：使用 dmidecode
            try:
                result = subprocess.check_output(
                    "sudo dmidecode -t processor | grep ID",
                    shell=True,
                    stderr=subprocess.DEVNULL
                ).decode('utf-8', errors='ignore')
                
                if "ID:" in result:
                    cpu_id = result.split("ID:")[1].strip().upper()
                    return cpu_id
            except:
                pass
                
        elif system == "Darwin":  # macOS
            # macOS: 使用 sysctl 获取CPU信息
            try:
                result = subprocess.check_output(
                    "sysctl -n machdep.cpu.brand_string",
                    shell=True,
                    stderr=subprocess.DEVNULL
                ).decode('utf-8', errors='ignore')
                
                # macOS 没有真正的CPU序列号，使用CPU品牌字符串的哈希
                cpu_id = hashlib.md5(result.strip().encode()).hexdigest().upper()
                return cpu_id
            except:
                pass
        
        # 如果所有方法都失败，返回默认值
        return "UNKNOWN_CPU_ID"
        
    except Exception as e:
        print(f"获取CPU ID失败: {e}")
        return "UNKNOWN_CPU_ID"


def get_mac_address():
    """
    获取本机MAC地址
    返回：
        MAC地址字符串（已标准化：去空格、转大写、无冒号）
    """
    try:
        # 获取MAC地址
        mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
        # 格式化为标准格式（不带冒号，纯大写）
        mac_address = mac.upper()
        return mac_address
    except Exception as e:
        print(f"获取MAC地址失败: {e}")
        return "000000000000"


def get_hardware_fingerprint():
    """
    获取完整的硬件指纹信息（包含原始值和MD5哈希）
    返回：
        字典，包含：
        - board_uuid_raw: 主板UUID原始值
        - cpu_id_raw: CPU ID原始值
        - mac_address_raw: MAC地址原始值
        - board_uuid_md5: 主板UUID的MD5哈希
        - cpu_id_md5: CPU ID的MD5哈希
        - mac_address_md5: MAC地址的MD5哈希
    """
    # 获取原始硬件信息
    board_uuid_raw = get_board_uuid()
    cpu_id_raw = get_cpu_id()
    mac_address_raw = get_mac_address()
    
    # 标准化处理：去空格、转大写
    board_uuid_clean = board_uuid_raw.strip().upper()
    cpu_id_clean = cpu_id_raw.strip().upper()
    mac_address_clean = mac_address_raw.strip().upper()
    
    # 计算MD5哈希
    board_uuid_md5 = hashlib.md5(board_uuid_clean.encode('utf-8')).hexdigest().upper()
    cpu_id_md5 = hashlib.md5(cpu_id_clean.encode('utf-8')).hexdigest().upper()
    mac_address_md5 = hashlib.md5(mac_address_clean.encode('utf-8')).hexdigest().upper()
    
    return {
        "board_uuid_raw": board_uuid_clean,
        "cpu_id_raw": cpu_id_clean,
        "mac_address_raw": mac_address_clean,
        "board_uuid_md5": board_uuid_md5,
        "cpu_id_md5": cpu_id_md5,
        "mac_address_md5": mac_address_md5
    }


def print_hardware_info():
    """
    打印硬件信息（用于调试）
    """
    print("=" * 80)
    print("硬件信息采集")
    print("=" * 80)
    
    fingerprint = get_hardware_fingerprint()
    
    print("\n【原始硬件信息】")
    print(f"主板UUID:  {fingerprint['board_uuid_raw']}")
    print(f"CPU ID:    {fingerprint['cpu_id_raw']}")
    print(f"MAC地址:   {fingerprint['mac_address_raw']}")
    
    print("\n【MD5哈希值】")
    print(f"主板UUID:  {fingerprint['board_uuid_md5']}")
    print(f"CPU ID:    {fingerprint['cpu_id_md5']}")
    print(f"MAC地址:   {fingerprint['mac_address_md5']}")
    
    print("\n" + "=" * 80)


# ========== 测试代码 ==========
if __name__ == "__main__":
    print_hardware_info()

