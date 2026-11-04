"""Build the public, tracking-free Stick World policy pages (Python stdlib)."""
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parent
ORIGIN = "https://kwak1696.github.io"
DATE = "2026-11-05"
EMAIL = "kwak1696@kakao.com"

CONTACT = f'<a href="mailto:{EMAIL}">{EMAIL}</a>'
PAGES = {
"index.html": ("Stick World · 프로젝트 및 정책", "project", f"""
<section class="hero"><p class="eyebrow">STICK WORLD / PROJECT & POLICIES</p>
<h1>지도를 걷는 작은 탐험.</h1><p class="lead">Stick World는 GPS 위치에 따라 스틱맨이 움직이는 지도 탐험 앱입니다. 이 사이트는 프로젝트 소개와 이용자 보호를 위한 정책을 제공합니다.</p>
<div class="actions"><a class="primary" href="/privacy.html">개인정보처리방침</a><a class="secondary" href="/terms.html">서비스 이용약관</a></div></section>
<section class="cards" aria-label="프로젝트 안내"><article><span class="number">01</span><h2>기기에서 시작하는 위치 기능</h2><p>START GPS를 선택하면 현재 위치를 지도에 표시합니다. 단독 모드가 기본이며, 위치 권한과 센서 사용은 기기에서 관리할 수 있습니다.</p></article>
<article><span class="number">02</span><h2>선택하는 기능, 분명한 안내</h2><p>온라인 위치 공유는 별도 참여가 필요합니다. 광고 SDK의 데이터 처리와 개인정보 선택은 정책에서 확인할 수 있습니다.</p></article>
<article><span class="number">03</span><h2>개발 중인 프로젝트</h2><p>현재 앱은 개발·검증 단계입니다. 이 사이트는 게임 서버, 결제 서비스 또는 앱 스토어 판매 페이지를 운영하지 않습니다.</p></article></section>
<section class="note"><h2>운영자와 연락처</h2><p>운영자: <strong>kwak1696</strong><br>프로젝트: <strong>Stick World / Stick Walk</strong><br>앱 패키지: <code>com.personallab.stickwalk</code><br>개인정보·서비스 문의: {CONTACT}</p><p><a href="/support.html">문의 및 데이터 삭제 안내</a> · <a href="/app-ads.txt">광고 판매자 정보(app-ads.txt)</a></p></section>
"""),
"privacy.html": ("개인정보처리방침 · Stick World", "privacy", f"""
<header class="document-head"><p class="eyebrow">PRIVACY POLICY</p><h1>개인정보처리방침</h1><p class="lead">Stick World / Stick Walk</p><p>시행일·최종 업데이트: <time datetime="{DATE}">{DATE}</time> · 운영자: kwak1696</p></header>
<aside class="note"><strong>핵심 안내</strong><p>기본 단독 모드의 GPS 위치·기기 방향은 지도와 캐릭터 표시를 위해 기기에서 사용합니다. 선택적 온라인 기능에서는 위치 공유가 발생합니다. Google 광고 SDK와 이 웹사이트의 호스팅 제공자는 각각의 기능을 위해 정보를 처리할 수 있습니다.</p></aside>
<section><h2>1. 적용 범위와 문의</h2><p>이 방침은 kwak1696이 제공하는 Stick World(앱에 Stick Walk로 표시될 수 있음, 패키지 <code>com.personallab.stickwalk</code>) 및 이 정책 사이트에 적용됩니다. 개인정보 관련 문의·열람·정정·삭제·처리정지·동의 철회 요청은 {CONTACT}로 보내실 수 있습니다. 요청하실 때 불필요한 정밀 위치, 신분증, 광고 식별자 또는 비밀번호를 보내지 마세요.</p></section>
<section><h2>2. 위치와 기기 방향</h2><p>앱은 사용자가 START GPS를 선택하고 운영체제 위치 권한을 허용하면 현재 위치와 위치 정확도 등을 이용해 지도 위 캐릭터 위치와 탐험 거리를 계산합니다. 기기 방향 추적 기능을 사용하는 경우 나침반·방향 센서 정보를 지도 시점에 반영합니다. 기본 단독 모드에서는 이러한 게임 위치·방향을 별도의 운영자 게임 서버에 전송하지 않습니다. 앱은 별도의 GPS 이동 이력 데이터베이스를 운영하지 않습니다.</p><p>현재 위치와 방향은 앱 세션 중 기기 메모리에서 사용됩니다. STOP GPS나 운영체제 권한 설정으로 새로운 위치 수집을 중지할 수 있습니다. 앱 일시정지 시 GPS 사용을 중단하도록 구현돼 있습니다. 수집 중지 후에도 마지막으로 표시한 위치가 현재 화면·세션에 남을 수 있습니다. 위치 권한을 거부하면 실제 위치 기반 기능이 제한되지만 다른 이용 가능한 기능은 사용할 수 있습니다.</p></section>
<section><h2>3. 선택적 온라인 위치 공유</h2><p>온라인 기능은 기본적으로 꺼져 있습니다. 사용자가 온라인 참여를 선택하면 지도상의 정밀 위치를 공통 좌표로 변환한 값, 캐릭터 방향, 메시지 순서 및 임시 세션 정보를 지정 서버에 전송하고 관심 반경 내 다른 참여자에게 아바타 위치를 표시합니다. 투영 좌표도 정밀 위치정보에 해당합니다. Android에서는 안내 후 별도 참여 동작이 필요하며 LEAVE ONLINE 또는 앱 일시정지 시 연결을 종료합니다.</p><p>현재 제공된 온라인 서버는 로컬 개발·검증용이며 일반 이용자를 위한 운영 서버는 제공하지 않습니다. 운영자는 운영 서버에 이용자의 정밀 위치 기록을 보관하는 서비스를 현재 운영하지 않습니다. 운영 온라인 서비스를 제공하게 되면 수신자·서버 제공자·처리 지역·보관기간 등 필요한 정보를 먼저 고지하고 이 방침 및 동의 절차를 갱신합니다. 개발용 클라이언트에서 직접 지정한 외부 서버에는 해당 서버 운영자의 처리 방식이 적용될 수 있으므로 신뢰할 수 있는 서버만 이용하세요.</p></section>
<section><h2>4. 지도 파일과 로컬 데이터</h2><p>기본 지도는 기기의 PMTiles 파일에서 읽습니다. 앱 데이터, 내려받은 지도·캐시 및 SDK 설정은 앱 저장 공간에 남을 수 있습니다. 지도 다운로드 기능을 이용하는 경우 지정된 다운로드 제공자는 통신에 필요한 IP 주소·요청 시각·전송 기록 등을 처리할 수 있습니다. 현재 앱의 기본 구성에는 운영자 소유의 전국 지도 다운로드 서버가 지정돼 있지 않습니다.</p><p>앱의 로컬 데이터는 운영체제의 앱 저장 공간 관리 기능으로 삭제할 수 있습니다. 앱 제거 또는 데이터 삭제 시의 실제 범위는 기기·OS·백업 설정에 따라 달라집니다. 이용자가 별도 경로에 복사한 지도나 백업본은 해당 경로에서 따로 삭제해야 합니다.</p></section>
<section><h2>5. 광고 및 Google SDK</h2><p>앱에는 Google Mobile Ads 및 User Messaging Platform(UMP) SDK가 포함돼 있습니다. 광고는 지도 조작 화면과 분리된 SUMMARY 화면에서 표시하도록 구성돼 있으며 현재 개발 기본값은 공식 테스트 광고입니다. 테스트 광고라고 해서 SDK의 모든 데이터 처리가 없어지는 것은 아닙니다.</p><p>Google 광고 SDK는 광고 제공·측정·분석·부정행위 방지 등을 위해 IP 주소(대략적 위치 추정에 사용될 수 있음), 기기·광고·앱 관련 식별자, 앱 실행·탭·동영상 조회 등 상호작용, 앱·SDK 성능과 진단정보 등을 수집·공유할 수 있습니다. 이 앱은 정밀 GPS 좌표나 나침반 정보를 광고 요청에 직접 추가하지 않습니다. 개인정보 선택·지역·SDK 설정 등에 따라 처리 및 광고 종류가 달라질 수 있습니다.</p><p>필요한 경우 UMP 메시지로 선택을 요청하고 개인정보 선택 메뉴에서 변경할 수 있도록 합니다. 앱 자체의 광고 초기화·요청은 SDK가 허용한 동의 상태를 확인한 뒤 수행합니다. Android 광고 식별자는 기기의 개인정보·광고 설정에서도 관리할 수 있습니다. 맞춤형 광고 동의를 거부하더라도 허용된 범위에서 비맞춤형·제한적 광고가 제공될 수 있습니다. SDK에는 네이티브 시작 구성요소가 있으므로 앱의 광고 요청 게이트가 SDK 전체의 시작 시 데이터 처리를 없앤다고 보장하지 않습니다.</p><p>Google이 처리하는 정보의 보관·삭제·권리 행사 및 국외 처리에는 Google의 정책과 해당 선택 화면이 적용됩니다. Google 등 제공자의 국제 인프라에 따라 정보가 대한민국 외 국가에서 처리될 수 있습니다. 별도 고지·동의가 필요한 기능은 그 요건을 갖춘 범위에서 제공합니다.</p><ul><li><a href="https://policies.google.com/privacy?hl=ko">Google 개인정보처리방침</a></li><li><a href="https://policies.google.com/technologies/partner-sites?hl=ko">Google이 파트너 서비스를 통해 정보를 사용하는 방법</a></li><li><a href="https://developers.google.com/admob/android/privacy/play-data-disclosure">Google 광고 SDK 데이터 공개 안내</a></li></ul></section>
<section><h2>6. 문의와 보관·파기</h2><p>이메일 문의 시 이용자가 제공한 이메일 주소, 문의 내용 및 답변에 필요한 정보를 문의 처리와 권리 요청 확인 목적으로 사용합니다. 이메일은 이용자와 운영자의 이메일 서비스 제공자를 거쳐 전달·보관됩니다. 문의 목적이 달성돼 더 이상 필요하지 않은 정보는 삭제하며, 법령상 의무 또는 분쟁 처리를 위해 필요한 정보는 해당 근거와 필요한 기간에 한해 보관합니다. 불필요한 민감정보를 요청하지 않으며 공개 GitHub 이슈에 개인정보를 게시하도록 요구하지 않습니다.</p><p>앱에는 현재 이용자 회원가입·유료 결제 기능이 없습니다. 삭제할 앱 회원 계정을 운영하지 않지만 로컬 데이터 및 문의 정보에 대한 권리는 행사할 수 있습니다. Google 등 제3자가 독립적으로 처리하는 정보는 해당 제공자의 설정·권리 행사 경로를 이용할 수 있으며, 운영자가 처리 가능한 범위에서 문의를 돕습니다.</p></section>
<section><h2>7. 이 웹사이트와 안전한 처리</h2><p>이 사이트에는 운영자가 설치한 광고, 방문 분석 스크립트, 별도 입력 폼 또는 추적 쿠키가 없습니다. GitHub Pages를 통해 제공되므로 GitHub는 보안·운영 등을 위해 방문자의 IP 주소 등 접속 정보를 처리할 수 있습니다. 호스팅 제공자의 기록은 운영자가 직접 운영하는 분석 데이터와 구분됩니다. 자세한 내용은 <a href="https://docs.github.com/en/site-policy/privacy-policies/github-privacy-statement">GitHub 개인정보처리방침</a>을 확인하세요.</p><p>사이트는 HTTPS로 제공하며 앱 저장 공간·접근 권한과 서비스 제공자의 보안 기능을 활용합니다. 운영 서비스에 원격 통신이 추가되는 경우 적절한 암호화·접근 통제를 적용합니다. 로컬 개발용 통신은 운영 서비스의 보안 수준을 나타내지 않습니다. 모든 기기·제3자 인프라에서 위험이 전혀 없다고 보장하지는 않습니다.</p></section>
<section><h2>8. 아동·법정대리인과 방침 변경</h2><p>법령상 보호자 동의가 필요한 아동의 개인정보는 필요한 절차 없이 의도적으로 처리하지 않습니다. 법정대리인은 위 연락처로 문의·삭제 등 요청을 할 수 있습니다. 아동 대상 기능·광고를 제공하는 경우 필요한 연령·보호자 동의 및 광고 설정을 먼저 갖춥니다.</p><p>기능·SDK·처리 방식 또는 관련 요건이 바뀌면 이 페이지의 업데이트 날짜와 내용을 변경합니다. 권리에 중요한 영향을 주는 변경은 적용 전에 합리적인 방법으로 알리고, 필요한 경우 별도의 동의를 받습니다.</p></section>
<section class="note"><h2>개인정보 문의</h2><p>운영자: kwak1696 · 앱: Stick World / Stick Walk<br>{CONTACT}</p><p><a href="/support.html">기기 데이터 삭제·문의 방법 보기</a></p></section>
"""),
"terms.html": ("서비스 이용약관 · Stick World", "terms", f"""
<header class="document-head"><p class="eyebrow">TERMS OF USE</p><h1>서비스 이용약관</h1><p class="lead">Stick World / Stick Walk</p><p>시행일·최종 업데이트: <time datetime="{DATE}">{DATE}</time> · 운영자: kwak1696</p></header>
<section><h2>1. 목적과 서비스</h2><p>이 약관은 kwak1696(이하 운영자)이 제공하는 Stick World / Stick Walk 앱과 관련 안내의 이용 조건을 정합니다. 앱은 GPS·기기 센서와 지도 데이터를 이용한 탐험 기능을 제공합니다. 현재 개발·검증 중인 기능이 포함되며 기기, 운영체제, 데이터 제공 범위 및 네트워크 상태에 따라 이용 가능 기능이 다릅니다.</p><p>앱은 길 안내·구조·안전 판단을 위한 전문 서비스가 아닙니다. 지도 형상, 높이, 위치와 방향에는 오차가 있을 수 있습니다. 실제 도로·시설의 통행 가능 여부나 출입 권한을 보증하지 않습니다.</p></section>
<section><h2>2. 안전한 이용과 권한</h2><p>주변 환경·교통 법규·시설 규칙을 우선 확인하고 안전한 곳에 멈춰 화면을 조작하세요. 운전 중 사용하거나 사유지·위험 구역에 무단 진입하지 마세요. 필요한 위치·센서·네트워크 권한은 기능 안내와 운영체제 설정에 따라 선택·관리할 수 있습니다.</p><p>온라인 참여는 선택 사항입니다. 참여하면 위치가 다른 참여자에게 표시될 수 있으므로 공유 범위를 확인하세요. 현재 일반 이용자를 위한 운영 온라인 서버는 제공하지 않습니다. 이용자가 별도 서버를 지정하는 경우 해당 서버의 신뢰성과 이용 조건을 확인해야 합니다.</p></section>
<section><h2>3. 요금과 광고</h2><p>현재 앱에는 이용자 회원가입, 유료 구독 또는 인앱 결제 기능이 없습니다. 데이터 통신료 등 기기·통신사 비용은 이용자의 계약에 따릅니다. 향후 유료 기능을 도입하는 경우 가격·결제·취소 등 조건을 별도로 안내하고 필요한 동의를 받습니다.</p><p>앱에는 제3자 광고 SDK가 포함됩니다. 현재 기본 구성은 테스트 광고이며 실제 광고 제공은 계정·앱 검토와 관련 요건을 갖춘 뒤 적용됩니다. 광고 내용과 연결된 외부 서비스는 해당 제공자의 조건에 따릅니다. 광고 클릭은 자발적인 관심에 따라야 하며 자동·반복 클릭, 허위 노출 또는 클릭 유도 등 부정 이용을 해서는 안 됩니다.</p></section>
<section><h2>4. 이용 시 지켜야 할 사항</h2><p>다른 사람의 위치·개인정보를 동의 없이 수집·추적·공개하거나, 타인의 권리를 침해하거나, 불법·유해 행위를 위해 서비스를 이용해서는 안 됩니다. 서비스·네트워크를 손상시키는 공격, 무단 접근, 사칭, 통신 조작 및 부정 광고 트래픽 생성도 금지합니다. 문서화된 PC 위치 시뮬레이션과 정상적인 개발·테스트는 그 목적에 맞게 이용할 수 있습니다.</p><p>운영자는 위반 또는 보안·권리 보호를 위해 필요한 범위에서 기능·접속을 제한할 수 있습니다. 가능한 경우 사유와 문의 방법을 안내하며, 긴급한 대응이 필요한 경우 우선 조치할 수 있습니다.</p></section>
<section><h2>5. 개인정보와 외부 서비스</h2><p>개인정보 처리는 <a href="/privacy.html">개인정보처리방침</a> 및 필요한 기능별 안내·선택에 따릅니다. Google 광고 서비스, GitHub 호스팅 또는 이용자가 방문하는 외부 사이트에는 해당 제공자의 조건·정책이 적용됩니다. 외부 링크는 그 서비스의 품질·안전성이나 모든 콘텐츠에 대한 운영자의 보증을 뜻하지 않습니다.</p></section>
<section><h2>6. 지식재산권과 지도 출처</h2><p>앱·문서의 권리는 각 권리자에게 있습니다. 운영자는 이용자에게 제공 기능을 정상적으로 이용할 수 있는 비독점적 이용 범위를 허용합니다. 법령 또는 해당 라이선스가 허용하는 권리를 이 약관으로 제한하지 않습니다.</p><p>지도 데이터는 © OpenStreetMap contributors 및 관련 데이터 제공자에 기반하며 ODbL 등 해당 조건이 적용됩니다. Google SDK와 기타 외부 구성요소에는 각각의 라이선스·약관이 적용됩니다. 앱의 지도 출처·저작권 및 배포 라이선스 공지를 확인하세요. <a href="https://www.openstreetmap.org/copyright">OpenStreetMap 저작권·라이선스 안내</a></p></section>
<section><h2>7. 기능 변경·중단과 책임</h2><p>개발·검증, 유지보수, 보안, 지도 또는 외부 제공자의 사정 등으로 기능을 변경·일시 중단할 수 있습니다. 이용에 중요한 변경은 가능한 범위에서 미리 알립니다. 정확도·연속 이용·특정 기기 성능 또는 특정 수익을 보장하지 않습니다.</p><p>운영자와 이용자의 책임은 관련 법령에 따릅니다. 이 약관은 운영자의 고의·중대한 과실로 인한 책임이나 법령상 배제할 수 없는 책임·소비자 권리를 제한하지 않습니다. 이용자는 자신의 안전과 적법한 이용을 위해 합리적인 주의를 기울여야 합니다.</p></section>
<section><h2>8. 변경·문의와 분쟁</h2><p>약관을 바꾸는 경우 이 페이지에 변경 내용과 적용일을 표시하고, 중요한 변경은 적용 전에 합리적인 방법으로 알리며 필요한 경우 별도의 동의를 받습니다. 문의·불만은 {CONTACT}로 접수할 수 있습니다.</p><p>대한민국 법령을 기준으로 해석하며 이용자에게 적용되는 강행규정상의 권리를 존중합니다. 분쟁은 우선 상호 협의하고 해결되지 않으면 관련 법령이 정한 관할 법원·분쟁 해결 절차를 따릅니다.</p></section>
"""),
"support.html": ("문의·데이터 관리 · Stick World", "support", f"""
<header class="document-head"><p class="eyebrow">SUPPORT & DATA CONTROLS</p><h1>문의와 데이터 관리</h1><p class="lead">Stick World / Stick Walk · 운영자 kwak1696</p></header>
<section><h2>직접 문의하기</h2><p>서비스·개인정보·삭제 요청: {CONTACT}</p><p>앱 이름, 기기·운영체제 및 문의 목적을 필요한 범위에서 알려주세요. 비밀번호, 신분증, 광고 식별자나 정확한 위치를 먼저 보내지 마세요. 공개 GitHub 이슈에 개인정보를 작성할 필요가 없습니다.</p></section>
<section><h2>기기에서 직접 관리하기</h2><ol><li><strong>GPS:</strong> 앱에서 STOP GPS를 누르거나 운영체제의 앱 위치 권한을 변경하세요.</li><li><strong>기기 방향:</strong> 앱에서 제공하는 방향 추적 설정을 끄거나 수동 시점을 사용하세요.</li><li><strong>온라인 공유:</strong> LEAVE ONLINE을 누르세요. 앱 일시정지 시에도 연결을 종료합니다.</li><li><strong>앱 데이터·지도:</strong> Android 설정의 앱 → Stick World 또는 Stick Walk → 저장 공간에서 데이터를 삭제하거나 앱을 제거하세요. 별도 저장 경로와 백업본은 따로 관리해야 할 수 있습니다.</li><li><strong>광고 선택:</strong> 앱에 표시되는 개인정보 선택 메뉴와 Android의 개인정보·광고 설정을 이용하세요. Google 처리 정보에 관한 요청은 Google의 개인정보 도구도 확인하세요.</li></ol></section>
<section><h2>계정 삭제와 문의 정보</h2><p>현재 앱은 이용자 회원 계정을 만들지 않으므로 삭제할 앱 계정이 없습니다. 앱 로컬 데이터 삭제 및 운영자가 보유한 문의 정보에 대한 열람·정정·삭제 등 요청은 가능합니다. 이메일 제목에 ‘개인정보 요청 — Stick World’를 적어 위 연락처로 보내주세요. 처리에 필요한 범위에서 요청 확인을 진행하고 관련 법령에 따라 답변합니다.</p></section>
<p><a href="/privacy.html">개인정보처리방침 전체 읽기</a> · <a href="/terms.html">서비스 이용약관 읽기</a></p>
""")
}

def build():
    nav = (("project", "/", "프로젝트"), ("privacy", "/privacy.html", "개인정보"),
           ("terms", "/terms.html", "이용약관"), ("support", "/support.html", "문의"))
    for file, (title, active, body) in PAGES.items():
        links = ''.join(f'<a href="{url}"'+(' aria-current="page"' if key == active else '')+f'>{label}</a>' for key,url,label in nav)
        canonical = ORIGIN + ('/' if file == 'index.html' else '/' + file)
        page = f'''<!doctype html>
<html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{escape(title)}</title><meta name="description" content="Stick World 프로젝트의 개인정보처리방침, 이용약관, 문의 및 데이터 관리 안내"><link rel="canonical" href="{canonical}"><link rel="stylesheet" href="/style.css"><meta name="theme-color" content="#163d33"></head>
<body><a class="skip" href="#main">본문으로 건너뛰기</a><header class="site-header"><a class="brand" href="/" aria-label="Stick World 홈"><span class="mark" aria-hidden="true">↗</span> STICK WORLD</a><nav aria-label="주 메뉴">{links}</nav></header>
<main id="main">{body}</main><footer><strong>STICK WORLD</strong><p>운영자 kwak1696 · {CONTACT}</p><p><a href="/privacy.html">개인정보처리방침</a> · <a href="/terms.html">이용약관</a> · <a href="/support.html">문의·데이터 관리</a></p><small>정책 업데이트 {DATE} · <a href="https://github.com/kwak1696/kwak1696.github.io">사이트 소스와 변경 이력</a></small></footer></body></html>'''
        (ROOT / file).write_text(page, encoding='utf-8')
    (ROOT / 'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join(f'<url><loc>{ORIGIN}{"/" if f == "index.html" else "/"+f}</loc><lastmod>{DATE}</lastmod></url>' for f in PAGES)+'</urlset>\n', encoding='utf-8')

if __name__ == '__main__':
    build()
