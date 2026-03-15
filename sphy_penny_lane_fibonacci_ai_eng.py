# ==================================================================================
# 🐦 HARPIA QUANTUM LABS - V18.2 CLOUD AKASHIC (FIXED & SECURE)
# 👤 Author: Deywe Okabe | 🤖 Co-Author: Gemini 3 Flash
# 💎 Edition: ETHEREAL AKASHIC (Handshake Protocol)
# ==================================================================================
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import pandas as pd
import sys, os, time, re
import requests
from tqdm import tqdm

# --- CONSTANTES GLOBAIS (Soberania Matemática) ---
PHI = (1 + np.sqrt(5)) / 2  # Definido globalmente para evitar NameError

# Configuração de Backend Matplotlib
try:
    matplotlib.use('Qt5Agg')
except:
    matplotlib.use('TkAgg')

# ==================================================================================
# MÓDULO I: ORÁCULO PENNYLANE (VETORIZADO)
# ==================================================================================
try:
    import pennylane as qml
    PENNYLANE_AVAILABLE = True
    dev_oracle = qml.device("default.qubit", wires=1)

    @qml.qnode(dev_oracle)
    def circuito_oraculo_batch(fases_input):
        qml.Hadamard(wires=0)
        qml.RZ(fases_input, wires=0)
        return qml.expval(qml.PauliZ(0)) 
except ImportError:
    PENNYLANE_AVAILABLE = False

def gerar_fluxo_quantico_akashic(t_array):
    if not PENNYLANE_AVAILABLE:
        return np.random.uniform(-0.05, 0.05, size=len(t_array))
    return np.array(circuito_oraculo_batch(t_array)) * 0.03

# ==================================================================================
# MÓDULO II: MOTORES HARPIA (KILL-SWITCH CLOUD)
# ==================================================================================
API_URL = "https://sphyfibonacciapi-cpifhimtglsq6imaebf33f.streamlit.app/"

def VR_Engine_Cloud(p_singular, caos_neg):
    """
    A simulação é BLOQUEADA se não houver handshake com a API.
    """
    try:
        response = requests.get(API_URL, timeout=5) 
        
        if response.status_code == 200:
            boost_web = 1.25 
            status_txt = "🌐 CLOUD SYNC ACTIVE"
            # O print abaixo confirma a validação antes de prosseguir
            print(f"   [OK] Protocolo SPHY Validado na Nuvem.")
        else:
            print(f"\n❌ ERRO CRÍTICO: API retornou Status {response.status_code}")
            sys.exit("⚠️ Acesso Negado: A simulação exige autorização do servidor.")
            
    except Exception as e:
        print(f"\n🚨 ERRO DE CONEXÃO: O link da API está offline ou inacessível.")
        print(f"   Detalhes: {e}")
        sys.exit("⚠️ Simulação Abortada: Conecte-se para validar o Motor Akashic.")

    ganho_base = np.exp(-np.abs(p_singular) * 0.01)
    amplificador = (1 + 0.99 * np.tanh(caos_neg))
    return ganho_base * amplificador * (1 + 0.2 * boost_web), status_txt

# ==================================================================================
# MÓDULO III: NÚCLEO AKASHIC (VETORIZADO)
# ==================================================================================
def coerencia_ethereal_vectorized(f_matrix, zeta_base, ruido_local, r_toro_base):
    ruido_filtrado = ruido_local * np.exp(-np.abs(ruido_local) * 1.5)
    peso_memoria = np.where(np.abs(ruido_local) > 0.1, 0.99, 0.95)
    s_longo = np.exp(-np.abs(ruido_filtrado) * 0.01)
    s_curto = np.exp(-np.abs(ruido_filtrado) * 0.5)
    s_coerencia = (peso_memoria * s_longo) + ((1 - peso_memoria) * s_curto)
    fase_vibracional = zeta_base + (ruido_filtrado * (1 - s_coerencia) * 0.01)
    distorcao = r_toro_base * (1 + (1 - s_coerencia) * 0.001 * np.sin(f_matrix / PHI))
    return fase_vibracional, distorcao, s_coerencia

def processar_frames_akashic(n_qubits, total_frames, R_TORO, r_TORO, F_ACHAT, habilitar_vr=True):
    print(f"⚙️  Iniciando Motor Akashic...")
    start_time = time.perf_counter()

    frames = np.arange(total_frames)
    qubits = np.arange(n_qubits)
    F_grid, Q_grid = np.meshgrid(frames, qubits, indexing='ij') 
    T_grid = F_grid * 0.05
    
    fluxo_t = gerar_fluxo_quantico_akashic(frames * 0.05)
    Fluxo_grid = np.tile(fluxo_t[:, np.newaxis], (1, n_qubits)) 

    Caos_base_grid = (F_grid / total_frames) * 12.0
    limit_critico = 2.618
    Caos_estabilizado_grid = np.where(Caos_base_grid >= (limit_critico * 0.85), limit_critico * 0.80, Caos_base_grid)
    
    P_singular_grid = np.random.uniform(0, 1, size=(total_frames, n_qubits)) * (Caos_estabilizado_grid * 0.1)

    # Chamada obrigatória para validar o link
    Ganho_grid, status_msg = VR_Engine_Cloud(P_singular_grid, -Caos_estabilizado_grid)
    Torque_grid = -P_singular_grid * Ganho_grid

    Zeta_ideal = (PHI * T_grid) + (Q_grid * (2 * np.pi / n_qubits)) + (P_singular_grid + Torque_grid) + (Fluxo_grid * 0.05)
    Zeta_real, R_din, S_local = coerencia_ethereal_vectorized(F_grid, Zeta_ideal, (P_singular_grid * 0.05), r_TORO)
    
    X_grid = (R_TORO + R_din * np.cos(T_grid)) * np.cos(Zeta_real)
    Y_grid = (R_TORO + R_din * np.cos(T_grid)) * np.sin(Zeta_real)
    Z_grid = (R_din * F_ACHAT) * np.sin(T_grid)

    print("📦 Organizando Telemetria em Bloco Único...")
    data_payload = {
        'Frame': frames,
        'T': frames * 0.05,
        'Cloud_Status': [status_msg] * total_frames
    }

    for i in range(n_qubits):
        data_payload[f'q{i}_x'] = X_grid[:, i]
        data_payload[f'q{i}_y'] = Y_grid[:, i]
        data_payload[f'q{i}_z'] = Z_grid[:, i]
        data_payload[f'q{i}_S'] = S_local[:, i]

    df_sim = pd.DataFrame(data_payload).copy()

    dt = time.perf_counter() - start_time
    print(f"⚡ Akashic Core Finalizado em {dt:.4f}s.")
    return df_sim, {"coerencia_media": np.mean(S_local)}

# ==================================================================================
# MÓDULO IV: VISUALIZAÇÃO ETHEREAL
# ==================================================================================
def visualizar_ethereal(df_sim, n_qubits, stats, R_TORO, r_TORO, F_ACHAT):
    print(f"\n🎨 Renderizando Modo Ethereal...")
    fig = plt.figure(figsize=(14, 10), facecolor='#050505')
    ax = fig.add_subplot(111, projection='3d', facecolor='#050505')
    ax.axis('off')
    ax.set_box_aspect([1, 1, 0.3]) 
    
    u, v = np.mgrid[0:2*np.pi:100j, 0:2*np.pi:50j]
    x_t = (R_TORO + r_TORO * np.cos(v)) * np.cos(u)
    y_t = (R_TORO + r_TORO * np.cos(v)) * np.sin(u)
    z_t = (r_TORO * F_ACHAT) * np.sin(v)
    ax.plot_wireframe(x_t, y_t, z_t, color='#00FFFF', alpha=0.1, linewidth=0.2)
    
    cores = plt.cm.cool(np.linspace(0, 1, n_qubits))
    lasers = [ax.plot([], [], [], color=cores[i], lw=0.8, alpha=0.6)[0] for i in range(n_qubits)]
    pontos = [ax.plot([], [], [], 'o', color='white', markersize=3, alpha=1.0)[0] for i in range(n_qubits)]
    
    texto_info = ax.text2D(0.02, 0.98, '', transform=ax.transAxes, color='white', fontfamily='monospace')

    def update(frame):
        row = df_sim.iloc[frame % len(df_sim)]
        cloud_status = row['Cloud_Status']
        s_medio = np.mean([row[f'q{i}_S'] for i in range(n_qubits)])

        texto_info.set_text(f"FRAME {frame} | FIDELIDADE: {s_medio:.4%}\nSTATUS: {cloud_status}")
        
        for i in range(n_qubits):
            lookback = max(0, frame - 15)
            lasers[i].set_data(df_sim[f'q{i}_x'].values[lookback:frame+1], df_sim[f'q{i}_y'].values[lookback:frame+1])
            lasers[i].set_3d_properties(df_sim[f'q{i}_z'].values[lookback:frame+1])
            pontos[i].set_data([row[f'q{i}_x']], [row[f'q{i}_y']])
            pontos[i].set_3d_properties([row[f'q{i}_z']])
        
        ax.view_init(elev=30, azim=frame * 0.4)
        return lasers + pontos + [texto_info]
    
    ani = FuncAnimation(fig, update, frames=len(df_sim), interval=20, blit=False)
    plt.show()

# ==================================================================================
# MAIN
# ==================================================================================
def harpia_main_v18_2():
    print("\n" + "💎"*40)
    print("      ✨ HARPIA V18.2 - ETHEREAL AKASHIC (SECURED)")
    print("💎"*40)
    
    try:
        n_qubits = int(input("🔢 Qubits: ") or 120)
        total_frames = int(input("🎞️  Frames: ") or 600)
    except:
        n_qubits, total_frames = 120, 600
    
    df_sim, stats = processar_frames_akashic(n_qubits, total_frames, 21.0, 2.5, 0.000001)
    
    print(f"\n✅ SUCESSO: Coerência Média {stats['coerencia_media']:.6%}")
    if input("\n🎨 Abrir Visualizador? (s/n): ").lower() != 'n':
        visualizar_ethereal(df_sim, n_qubits, stats, 21.0, 2.5, 0.000001)

if __name__ == "__main__":
    harpia_main_v18_2()
